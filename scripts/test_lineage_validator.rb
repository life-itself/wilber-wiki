#!/usr/bin/env ruby
# Synthetic mutations are validator fixtures, never historical research records.
require 'minitest/autorun'
require 'yaml'
require 'json'
require 'tmpdir'
require 'open3'

class LineageValidatorTest < Minitest::Test
  ROOT = File.expand_path('..', __dir__)
  SCRIPT = File.join(ROOT, 'scripts/validate_lineage.rb')
  LEDGER = File.join(ROOT, 'docs/plans/2026-09-17-works-concept-lineage-data.yaml')

  def setup
    @data = YAML.safe_load(File.read(LEDGER))
  end

  def run_check(valid, pattern = nil)
    assert File.file?(SCRIPT), 'Reusable lineage validator must exist'
    Dir.mktmpdir('lineage-test-') do |dir|
      file = File.join(dir, 'synthetic.yaml')
      # Independent values prevent fixture object sharing from emitting YAML aliases.
      File.write(file, YAML.dump(JSON.parse(JSON.generate(@data))))
      output, status = Open3.capture2e('ruby', SCRIPT, file, ROOT)
      assert_equal valid, status.success?, output
      assert_match pattern, output if pattern
    end
  end

  def test_real_ledger
    run_check(true, /PASS/)
  end

  def test_excerpt_target_without_catalog_work
    @data['appearances'][0].delete('work')
    @data['appearances'][0]['source_unit'] = 'kosmos-ii-excerpt-a'
    run_check(true)
  end

  def test_ambiguous_target
    @data['appearances'][0]['source_unit'] = 'kosmos-ii-excerpt-a'
    run_check(false, /exactly one target/)
  end

  def test_missing_target
    @data['appearances'][0].delete('work')
    run_check(false, /exactly one target/)
  end

  def test_unknown_reference
    @data['appearances'][0]['concept'] = 'nonexistent'
    run_check(false, /unknown concept/)
  end

  def test_duplicate_id
    @data['appearances'] << @data['appearances'][0].dup
    run_check(false, /duplicate/)
  end

  def test_invalid_role_and_confidence
    @data['appearances'][0]['role'] = 'influences'
    @data['appearances'][0]['confidence'] = 'certain'
    run_check(false, /invalid/)
  end

  def test_development_without_comparison
    @data['appearances'][1]['role'] = 'develops'
    run_check(false, /comparison/)
  end

  def add_comparison
    earlier = Marshal.load(Marshal.dump(@data['appearances'][1]))
    earlier['id'] = 'synthetic-earlier'
    earlier['work'] = '1995-sex-ecology-spirituality'
    @data['appearances'] << earlier
    later = @data['appearances'][1]
    later['role'] = 'develops'
    later['comparison_ids'] = ['synthetic-comparison']
    @data['comparisons'] << {
      'id' => 'synthetic-comparison', 'earlier' => [earlier['id']],
      'later' => later['id'], 'type' => 'develops',
      'claim' => 'SYNTHETIC fixture, not a historical claim.',
      'rationale' => 'Exercise endpoint validation only.',
      'confidence' => 'low', 'confidence_reason' => 'Synthetic.',
      'scope' => 'examined-corpus', 'date' => later['date'].dup,
      'evidence' => [earlier, later].map do |a|
        a['evidence'][0].merge('supports' => a['id'])
      end
    }
  end

  def test_cross_work_comparison_shape
    add_comparison
    run_check(true)
  end

  def test_missing_earlier_evidence
    add_comparison
    @data['comparisons'][0]['evidence'].shift
    run_check(false, /evidence for endpoint/)
  end

  def test_self_comparison
    add_comparison
    @data['comparisons'][0]['earlier'] = [@data['comparisons'][0]['later']]
    run_check(false, /distinct/)
  end

  def test_missing_date_basis
    @data['appearances'][0].delete('date')
    run_check(false, /date/)
  end

  def test_unresolved_date_cannot_silently_use_publication_year
    @data['appearances'][0]['date'] = {'basis' => 'unresolved', 'year' => 2000, 'reason' => 'Not verified.'}
    run_check(false, /unresolved.*null/)
  end

  def test_unverified_excerpt
    @data['appearances'][0]['evidence'][0]['verification_excerpt'] = 'SYNTHETIC NONEXISTENT QUOTATION'
    run_check(false, /excerpt/)
  end

  def add_term
    a = @data['appearances'][0]
    @data['terminology'] << a.reject { |k, _| %w[role integrates_concepts].include?(k) }
      .merge('id' => 'synthetic-term', 'term' => 'SYNTHETIC term fixture')
  end

  def test_terminology
    add_term
    run_check(true)
  end

  def test_terminology_requires_evidence
    add_term
    @data['terminology'][0]['evidence'] = []
    run_check(false, /evidence/)
  end

  def add_edition
    a = @data['appearances'][0]
    @data['work_relationships'] << {
      'id' => 'synthetic-edition', 'from' => @data['works'][0]['id'],
      'to' => @data['works'][1]['id'], 'type' => 'revised-edition',
      'claim' => 'SYNTHETIC fixture, not an edition assertion.',
      'rationale' => 'Tests reference structure only.',
      'evidence' => a['evidence'], 'confidence' => 'low',
      'confidence_reason' => 'Synthetic.', 'scope' => 'examined-corpus',
      'date' => a['date'], 'revision_extent' => 'unknown'
    }
  end

  def test_edition_relationship
    add_edition
    run_check(true)
  end

  def test_compared_extent_needs_comparison_citation
    add_edition
    @data['work_relationships'][0]['revision_extent'] = 'compared'
    run_check(false, /comparison_citation/)
  end

  def test_introduction_requires_search_basis
    @data['appearances'][0]['role'] = 'introduces'
    run_check(false, /priority_basis/)
  end
end
