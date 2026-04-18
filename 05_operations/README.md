# 05_operations

Purpose: operational files supporting repeatable project maintenance.

## Structure

- `logs/` — operational logs not tied to scientific output tables.
- `manifests/` — run manifests and execution metadata.
- `automation/` — helper scripts for inventory/moves/index updates.
- `colab_bundles/` — portable operational mirrors of repo content, not manuscript authority.

## Usage

- Keep operational scripts and metadata here, not at root.
- Prefer append-only logs for auditability.
- Do not treat bundle mirrors as source-of-truth manuscript assets.
