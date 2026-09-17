#!/usr/bin/env python3
"""Create a standard UI Engineering feature workspace.

Feature artifacts are grouped together under .ui-engineering/specs/<feature>/
(spec-kit style) instead of being spread across type-named top-level
folders. Only decisions/patterns.json is genuinely project-wide (it spans
features by design) and stays outside specs/.
"""
import sys
from pathlib import Path

feature = sys.argv[1] if len(sys.argv) > 1 else None
if not feature:
    print("Usage: python scripts/create_artifact.py <feature>")
    sys.exit(2)

root = Path(".ui-engineering")
feature_root = root / "specs" / feature
paths = [
    root / "decisions",
    feature_root / "references",
    feature_root / "knowledge",
]
for path in paths:
    path.mkdir(parents=True, exist_ok=True)

(root / "status.yaml").touch(exist_ok=True)
print(f"Initialized UI Engineering workspace for: {feature} at {feature_root}")
