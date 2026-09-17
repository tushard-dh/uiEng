#!/usr/bin/env python3
"""Show deterministic UI Engineering workspace status.

Reflects the feature-first layout: each feature's artifacts live together
under .ui-engineering/specs/<feature>/ instead of type-named top-level
folders.
"""
from pathlib import Path

root = Path(".ui-engineering")
if not root.exists():
    print("No .ui-engineering directory found.")
    raise SystemExit(1)

for name in ["project-context.md", "status.yaml", "component-catalog.json"]:
    print(f"{name}: {'present' if (root / name).exists() else 'missing'}")

patterns_path = root / "decisions" / "patterns.json"
print(f"decisions/patterns.json: {'present' if patterns_path.exists() else 'missing'}")

specs_root = root / "specs"
features = sorted(p for p in specs_root.iterdir() if p.is_dir()) if specs_root.exists() else []
print(f"specs: {len(features)} feature(s)")

for feature_dir in features:
    spec = "present" if (feature_dir / "spec.json").exists() else "missing"
    decisions = "present" if (feature_dir / "decisions.json").exists() else "missing"
    synthesis = "present" if (feature_dir / "synthesis.json").exists() else "missing"
    references = feature_dir / "references"
    knowledge = feature_dir / "knowledge"
    ref_count = len(list(references.glob("*.json"))) if references.exists() else 0
    knowledge_count = len(list(knowledge.glob("*.json"))) if knowledge.exists() else 0
    print(
        f"  {feature_dir.name}: spec={spec} decisions={decisions} "
        f"synthesis={synthesis} references={ref_count} knowledge={knowledge_count}"
    )
