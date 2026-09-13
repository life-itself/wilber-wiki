#!/usr/bin/env bash
# Publish to the wilberwiki-preview CLI site WITHOUT exposing .beads/ or
# NEXT.md — the fl CLI's direct-upload path ignores config.json's
# contentExclude entirely (confirmed by testing 2026-09-13; also true for
# docs/ and library/, per AGENTS.md), so `fl . --yes` run directly would
# republish them at guessable URLs even though they're excluded from
# production. This script moves them out of the working tree for the
# duration of the publish (so fl's delta-sync deletes them from the
# remote / never uploads them), then restores them locally.
#
# Usage: ./scripts/publish-preview.sh
# (from the repo root; requires `fl` to be authenticated already)

set -euo pipefail
cd "$(dirname "$0")/.."

HOLDING="$(mktemp -d)"
trap 'mv "$HOLDING/.beads" .beads 2>/dev/null || true; mv "$HOLDING/NEXT.md" NEXT.md 2>/dev/null || true; rmdir "$HOLDING" 2>/dev/null || true' EXIT

if [ -e .beads ]; then mv .beads "$HOLDING/.beads"; fi
if [ -e NEXT.md ]; then mv NEXT.md "$HOLDING/NEXT.md"; fi

fl . --yes

echo "Restored .beads/ and NEXT.md locally (trap on exit)."
