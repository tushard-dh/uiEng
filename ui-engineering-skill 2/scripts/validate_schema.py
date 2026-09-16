#!/usr/bin/env python3
"""Deterministically validate JSON artifacts against nearby JSON schemas."""
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

pairs = [
    ("references", "ui-reference.schema.json"),
    ("knowledge", "ui-knowledge.schema.json"),
    ("decisions", "ui-decision.schema.json"),
    ("synthesis", "ui-synthesis.schema.json"),
    ("specs", "ui-spec.schema.json"),
]

errors = 0
for directory, schema_name in pairs:
    schema_path = schema_dir / schema_name
    if not schema_path.exists():
        continue
    schema = json.loads(schema_path.read_text())
    base = root / directory
    if not base.exists():
        continue
    for path in base.rglob("*.json"):
        try:
            data = json.loads(path.read_text())
            jsonschema.validate(data, schema)
            print(f"OK   {path}")
        except Exception as exc:
            errors += 1
            print(f"FAIL {path}: {exc}")

sys.exit(1 if errors else 0)
