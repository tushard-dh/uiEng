#!/usr/bin/env python3
"""Create a standard UI Engineering feature workspace."""
import sys
from pathlib import Path

feature = sys.argv[1] if len(sys.argv) > 1 else None
if not feature:
    print("Usage: python scripts/create_artifact.py <feature>")
    sys.exit(2)

root = Path(".ui-engineering")
paths = [
    root / "decisions",
    root / "references",
    root / "knowledge",
    root / "synthesis",
    root / "specs" / feature,
]
for path in paths:
    path.mkdir(parents=True, exist_ok=True)

(root / "status.yaml").touch(exist_ok=True)
print(f"Initialized UI Engineering workspace for: {feature}")
