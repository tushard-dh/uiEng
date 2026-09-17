#!/usr/bin/env python3
"""Deterministically validate JSON artifacts against nearby JSON schemas.

Layout is feature-first: per-feature artifacts live under
.ui-engineering/specs/<feature>/ (spec.json, decisions.json, synthesis.json,
references/*.json, knowledge/*.json). Only decisions/patterns.json and
component-catalog.json are project-wide and validated at the top level.
"""
import json, sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("jsonschema is not installed. Install with: pip install jsonschema")
    sys.exit(2)

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".ui-engineering")
schema_dir = root.parent / "schemas"
if not schema_dir.exists():
    schema_dir = Path("schemas")

errors = 0


def load_schema(name):
    path = schema_dir / name
    return json.loads(path.read_text()) if path.exists() else None


def check(path, schema):
    global errors
    if schema is None:
        return
    try:
        data = json.loads(path.read_text())
        jsonschema.validate(data, schema)
        print(f"OK   {path}")
    except Exception as exc:
        errors += 1
        print(f"FAIL {path}: {exc}")


pattern_schema = load_schema("ui-pattern.schema.json")
patterns_path = root / "decisions" / "patterns.json"
if patterns_path.exists():
    check(patterns_path, pattern_schema)

catalog_schema = load_schema("component-catalog.schema.json")
catalog_path = root / "component-catalog.json"
if catalog_path.exists():
    check(catalog_path, catalog_schema)

spec_schema = load_schema("ui-spec.schema.json")
decision_schema = load_schema("ui-decision.schema.json")
synthesis_schema = load_schema("ui-synthesis.schema.json")
reference_schema = load_schema("ui-reference.schema.json")
knowledge_schema = load_schema("ui-knowledge.schema.json")

specs_root = root / "specs"
if specs_root.exists():
    for feature_dir in sorted(p for p in specs_root.iterdir() if p.is_dir()):
        for filename, schema in [
            ("spec.json", spec_schema),
            ("decisions.json", decision_schema),
            ("synthesis.json", synthesis_schema),
        ]:
            path = feature_dir / filename
            if path.exists():
                check(path, schema)
        for subdir, schema in [
            ("references", reference_schema),
            ("knowledge", knowledge_schema),
        ]:
            sub = feature_dir / subdir
            if sub.exists():
                for path in sub.glob("*.json"):
                    check(path, schema)

sys.exit(1 if errors else 0)
