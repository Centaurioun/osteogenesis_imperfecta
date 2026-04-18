# 99_archive

Purpose: no-delete historical archive with provenance.

## Structure

- `by_release/` — archives grouped by analysis release lineage.
- `by_date/` — archives grouped by reorganization/archive wave date.
- `snapshots/` — root inventory and move logs.
- `indexes/` — lookup indices (`archive_lookup.csv`).

## Rules

- Do not modify archived analytical content unless correcting metadata/indexes.
- Record every move in a move log and keep lookup indexes current.
- Keep this folder discoverable (indexes uncompressed), even if old payloads are compressed.
