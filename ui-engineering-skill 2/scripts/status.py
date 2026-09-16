#!/usr/bin/env python3
"""Show deterministic UI Engineering workspace status."""
from pathlib import Path

root = Path(".ui-engineering")
if not root.exists():
    print("No .ui-engineering directory found.")
    raise SystemExit(1)

for name in ["project-context.md", "status.yaml"]:
    print(f"{name}: {'present' if (root/name).exists() else 'missing'}")

for directory in ["references", "knowledge", "decisions", "synthesis", "specs"]:
    path = root / directory
    count = len(list(path.rglob("*"))) if path.exists() else 0
    print(f"{directory}: {count} artifact(s)")
