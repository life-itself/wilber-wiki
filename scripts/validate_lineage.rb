#!/usr/bin/env ruby
# Structural/evidence-location validation only; historical entailment needs review.
require 'yaml'

class LineageValidator
  COLLECTIONS = %w[concepts works source_units sources appearances terminology comparisons work_relationships unresolved_findings].freeze

  def initialize(data, root)
    @data, @root, @errors, @indices = data, root, [], {}
  end

  def check(condition, message)
    @errors << message unless condition
  end

  def present(value)
    !value.nil? && !(value.respond_to?(:empty?) && value.empty?) && !(value.is_a?(String) && value.strip.empty?)
  end

  def required(record, keys, label)
    keys.each { |key| check(present(record[key]), "#{label}: missing #{key}") }
  end

  def vocab(group, value, label)
    check(@data.fetch('vocabularies').fetch(group).key?(value), "#{label}: invalid #{group} #{value.inspect}")
  end

  def known(group, id, label)
    check(@indices.fetch(group).key?(id), "#{label}: unknown #{group.sub(/s$/, '')} #{id.inspect}")
  end

  def target(record, label)
    fields = %w[work source_unit].select { |k| record.key?(k) }
    check(fields.length == 1, "#{label}: requires exactly one target (work or source_unit)")
    fields.each { |key| known(key == 'work' ? 'works' : 'source_units', record[key], label) }
  end

  def date(record, label)
    d = record['date']
    unless d.is_a?(Hash)
      check(false, "#{label}: missing date object")
      return
    end
    required(d, %w[basis reason], "#{label} date")
    vocab('date_bases', d['basis'], label)
    check(d.key?('year') && (d['year'].nil? || d['year'].is_a?(Integer)), "#{label}: date year must be integer or null")
    check(d['year'].nil?, "#{label}: unresolved date must have null year") if d['basis'] == 'unresolved'
    check(d['year'].is_a?(Integer), "#{label}: original-edition-verified requires a year") if d['basis'] == 'original-edition-verified'
  end

  def evidence(record, label)
    items = record['evidence']
    unless items.is_a?(Array) && !items.empty?
      check(false, "#{label}: requires nonempty evidence list")
      return
    end
    items.each do |e|
      required(e, %w[source kind citation locator], "#{label} evidence")
      known('sources', e['source'], label)
      vocab('source_kinds', e['kind'], label)
      next unless e.key?('verification_excerpt')
      source = @indices['sources'][e['source']]
      path = source && source['path'] && File.join(@root, source['path'])
      check(present(e['verification_excerpt']) && path && File.file?(path) &&
        File.read(path).include?(e['verification_excerpt']), "#{label}: verification excerpt not found in local source")
    end
  end

  def run
    check(@data['schema_version'] == 2, 'Expected schema_version 2')
    all_ids = []
    COLLECTIONS.each do |name|
      records = @data.fetch(name)
      raise TypeError, "#{name} must be a list" unless records.is_a?(Array)
      @indices[name] = {}
      records.each do |r|
        id = r['id']
        check(id.is_a?(String) && id.match?(/\A[a-z0-9]+(?:-[a-z0-9]+)*\z/), "#{name}: invalid ID")
        check(!all_ids.include?(id), "#{name}: duplicate ID #{id}")
        all_ids << id
        @indices[name][id] = r
      end
    end
    @data['works'].each do |w|
      check(File.file?(File.join(@root, 'works', "#{w['id']}.md")), "#{w['id']}: missing work file")
      check(w['publication_year'].is_a?(Integer), "#{w['id']}: invalid publication_year")
      vocab('coverage_statuses', w['coverage'], w['id'])
    end
    @data['source_units'].each { |s| vocab('coverage_statuses', s['coverage'], s['id']) }
    @data['sources'].each do |s|
      required(s, %w[citation kind], s['id'])
      vocab('source_kinds', s['kind'], s['id'])
      check(present(s['path']) || present(s['url']), "#{s['id']}: source needs path or URL")
      check(File.file?(File.join(@root, s['path'])), "#{s['id']}: missing source file") if s['path']
    end
    %w[appearances terminology comparisons work_relationships unresolved_findings].each do |collection|
      @data[collection].each do |r|
        label = r['id']
        required(r, @data['contract'][collection]['required'], label)
        check(r['scope'] == 'examined-corpus', "#{label}: invalid scope")
        evidence(r, label)
        next if collection == 'unresolved_findings'
        vocab('confidence', r['confidence'], label)
        date(r, label)
        if %w[appearances terminology].include?(collection)
          target(r, label)
          known('concepts', r['concept'], label)
        end
      end
    end
    @data['appearances'].each do |a|
      id = a['id']
      vocab('roles', a['role'], id)
      if a['role'] == 'integrates'
        check(a['integrates_concepts'].is_a?(Array) && !a['integrates_concepts'].empty?, "#{id}: integrates requires concepts")
        Array(a['integrates_concepts']).each { |c| known('concepts', c, id) }
      end
      if %w[develops revises restates applies].include?(a['role'])
        check(a['comparison_ids'].is_a?(Array) && !a['comparison_ids'].empty?, "#{id}: role requires comparison_ids")
      end
      Array(a['comparison_ids']).each do |cid|
        c = @indices['comparisons'][cid]
        check(c && c['later'] == id && c['type'] == a['role'], "#{id}: comparison must match later endpoint and role")
      end
      next unless a['role'] == 'introduces'
      basis = a['priority_basis']
      unless basis.is_a?(Hash)
        check(false, "#{id}: missing priority_basis")
        next
      end
      required(basis, %w[examined_targets search_method], "#{id} priority_basis")
      check(basis['remaining_gaps'].is_a?(Array), "#{id}: priority_basis requires remaining_gaps list")
      Array(basis['examined_targets']).each { |t| target(t, "#{id} priority_basis") }
    end
    @data['comparisons'].each do |c|
      id = c['id']
      vocab('comparison_types', c['type'], id)
      earlier = c['earlier']
      check(earlier.is_a?(Array) && !earlier.empty?, "#{id}: earlier must be a nonempty list")
      endpoints = Array(earlier) + [c['later']]
      check(endpoints.uniq == endpoints, "#{id}: endpoints must be distinct")
      endpoints.each do |aid|
        known('appearances', aid, id)
        a = @indices['appearances'][aid]
        next unless a
        sources = Array(a['evidence']).map { |e| e['source'] }
        check(Array(c['evidence']).any? { |e| e['supports'] == aid && sources.include?(e['source']) }, "#{id}: missing evidence for endpoint #{aid}")
      end
      Array(c['evidence']).each { |e| check(endpoints.include?(e['supports']), "#{id}: evidence supports unknown endpoint") }
      later = @indices['appearances'][c['later']]
      Array(earlier).each do |aid|
        a = @indices['appearances'][aid]
        y1, y2 = a && a.dig('date', 'year'), later && later.dig('date', 'year')
        check(y1 <= y2, "#{id}: reversed dates") if y1.is_a?(Integer) && y2.is_a?(Integer)
      end
    end
    @data['work_relationships'].each do |r|
      %w[from to].each { |k| known('works', r[k], r['id']) }
      check(r['from'] != r['to'], "#{r['id']}: endpoints must be distinct")
      vocab('work_relationship_types', r['type'], r['id'])
      check(%w[unknown compared].include?(r['revision_extent']), "#{r['id']}: invalid revision_extent")
      required(r, %w[comparison_citation], r['id']) if r['revision_extent'] == 'compared'
    end
    @data['unresolved_findings'].each do |r|
      Array(r['works']).each { |id| known('works', id, r['id']) }
    end
    @errors
  end
end

if $PROGRAM_NAME == __FILE__
  root = ARGV[1] || File.expand_path('..', __dir__)
  file = ARGV[0] || File.join(root, 'docs/plans/2026-09-17-works-concept-lineage-data.yaml')
  begin
    data = YAML.safe_load(File.read(file))
    errors = LineageValidator.new(data, root).run
    if errors.empty?
      puts "PASS: lineage schema v2; #{data['appearances'].length} appearances; #{data['comparisons'].length} comparisons; #{data['unresolved_findings'].length} unresolved findings. Structural checks do not certify historical claims."
    else
      warn errors.join("\n")
      exit 1
    end
  rescue Psych::Exception, KeyError, TypeError, NoMethodError, ArgumentError, Errno::ENOENT => e
    warn "Invalid ledger: #{e.message}"
    exit 1
  end
end
