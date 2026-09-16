#!/usr/bin/env python3
"""Lightweight deterministic UI compliance checks.

This intentionally does not attempt to understand UX semantics. Claude's
reasoning layer performs semantic review.
"""
import re, sys
from pathlib import Path

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
extensions = {".tsx", ".jsx", ".ts", ".js", ".css", ".scss", ".html"}
findings = []

for path in root.rglob("*"):
    if not path.is_file() or path.suffix not in extensions:
        continue
    if any(part in {".git", "node_modules", "dist", "build"} for part in path.parts):
        continue
    try:
        text = path.read_text(errors="ignore")
    except Exception:
        continue

    if re.search(r'#[0-9a-fA-F]{3,8}\b', text):
        findings.append((path, "raw color literal detected; prefer design tokens"))
    if re.search(r'\b(margin|padding|gap)\s*:\s*\d+(px|rem)\b', text):
        findings.append((path, "hardcoded spacing detected; prefer design tokens"))

for path, message in findings[:100]:
    print(f"WARN {path}: {message}")

print(f"Checked source tree. Findings: {len(findings)}")
sys.exit(0)
