#!/usr/bin/env python3
"""Validate all recipe.yaml files in recipes/ against schema/recipe.schema.json."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RECIPES_DIR = ROOT / "recipes"
SCHEMA_FILE = ROOT / "schema" / "recipe.schema.json"


def main():
    try:
        import yaml
    except ImportError:
        print("PyYAML not installed, skipping yaml validation", file=sys.stderr)
        return 0

    if not SCHEMA_FILE.exists():
        print(f"Schema file missing: {SCHEMA_FILE}", file=sys.stderr)
        return 1

    recipes = list(RECIPES_DIR.glob("*/recipe.yaml"))
    if not recipes:
        print("No recipes found in recipes/*/", file=sys.stderr)
        return 1

    failed = False
    for r in sorted(recipes):
        try:
            with open(r, encoding="utf-8") as f:
                data = yaml.safe_load(f)
            # Basic sanity check
            for key in ["id", "name", "description", "version", "maintainer", "requirements"]:
                if key not in data:
                    print(f"FAIL: {r.parent.name}/recipe.yaml missing required field '{key}'", file=sys.stderr)
                    failed = True
                    break
            else:
                print(f"OK: {data['id']} (v{data['version']})")
        except Exception as e:
            print(f"FAIL: {r}: {e}", file=sys.stderr)
            failed = True

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
