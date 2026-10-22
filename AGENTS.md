# AGENTS.md — omnipha/recipes

This repository holds modular software recipes for Omnipha Linux phones.

## Rules for human and AI contributors

- **English only**: all docs, code comments, recipes, and commit messages.
- **Self-contained**: each recipe lives in `recipes/<id>/` and must not depend on files in other recipe directories.
- **Headless-first**: all core services must be fully operational without a physical display attached unless the recipe explicitly targets display interaction (e.g. `kiosk`).
- **One recipe per pull request**: keep pull requests atomic and focused.
- **Sign commits**: `git commit -s`.
- **Follow schema**: `recipe.yaml` must validate against `schema/recipe.schema.json`.

## Recipe lifecycle

- `draft`: skeleton with spec and proposed configuration.
- `functional`: tested on at least one device running Omnipha Linux.
- `verified`: running in production or field test with confirmed sensor/hardware mapping.

## Testing a recipe locally

```bash
# Validate schema
python3 tools/validate.py

# Lint compose files (if present)
docker compose -f recipes/<id>/docker-compose.yaml config
```
