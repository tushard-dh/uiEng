#!/usr/bin/env python3
"""Scan a product repository for existing UI components.

Deterministic file-system scan only — no design/UX reasoning happens here.
Ambiguous or unparseable components are flagged `needs_review` for a
follow-up Claude pass to classify semantically (see
workflows/component-catalog.md). This keeps the scan reusable across any
product repo without hardcoding assumptions about a specific codebase.
"""
import argparse
import datetime
import json
import re
from pathlib import Path

DEFAULT_EXTENSIONS = [".tsx", ".jsx", ".vue", ".svelte"]

COMPONENT_NAME_RE = re.compile(r"^[A-Z][A-Za-z0-9]*$")
EXPORT_DEFAULT_FUNC_RE = re.compile(r"export\s+default\s+function\s+([A-Za-z0-9_]+)")
EXPORT_DEFAULT_CONST_RE = re.compile(r"export\s+default\s+([A-Za-z0-9_]+)\s*;?\s*$", re.MULTILINE)
EXPORT_NAMED_RE = re.compile(r"export\s+(?:const|function)\s+([A-Z][A-Za-z0-9_]*)")
PROPS_TYPE_RE = re.compile(r"(?:interface|type)\s+([A-Za-z0-9_]*Props)\s*(?:=|\{)")
PROP_LINE_RE = re.compile(r"^\s*([A-Za-z0-9_]+)(\?)?\s*:\s*([^;{\n]+);?\s*$", re.MULTILINE)


def detect_framework(files):
    if any(f.suffix == ".vue" for f in files):
        return "vue"
    if any(f.suffix == ".svelte" for f in files):
        return "svelte"
    if any(f.suffix in (".tsx", ".jsx") for f in files):
        return "react"
    return "unknown"


def find_component_name(text, fallback):
    """Return (name, confident). confident=False means no export matched
    and the file stem was used as a last-resort guess."""
    for pattern in (EXPORT_DEFAULT_FUNC_RE, EXPORT_DEFAULT_CONST_RE, EXPORT_NAMED_RE):
        m = pattern.search(text)
        if m and COMPONENT_NAME_RE.match(m.group(1)):
            return m.group(1), True
    return fallback, False


def find_props(text):
    m = PROPS_TYPE_RE.search(text)
    if not m:
        return [], False
    brace_start = text.index("{", m.end() - 1)
    depth = 0
    body_end = brace_start
    for i, ch in enumerate(text[brace_start:], brace_start):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                body_end = i
                break
    body = text[brace_start + 1:body_end]
    props = []
    for pm in PROP_LINE_RE.finditer(body):
        props.append({
            "name": pm.group(1),
            "required": pm.group(2) != "?",
            "type": pm.group(3).strip(),
        })
    return props, len(props) > 0


def scan(root: Path, rel_paths, extensions):
    components = []
    seen_files = []
    for rel in rel_paths:
        base = root / rel
        if not base.exists():
            continue
        for ext in extensions:
            for file in sorted(base.rglob(f"*{ext}")):
                if file.stem.lower() == "index":
                    continue
                seen_files.append(file)
                text = file.read_text(encoding="utf-8", errors="ignore")
                fallback = file.stem
                name, confident_name = find_component_name(text, fallback)
                props, _found_props = find_props(text)
                components.append({
                    "name": name,
                    "path": str(file.relative_to(root)),
                    "category": "unknown",
                    "description": "",
                    "props": props,
                    "design_tokens_used": [],
                    "variants": [],
                    # Only flag low-confidence name resolution. Missing a
                    # parsed Props type is common and not itself a signal
                    # that something is wrong.
                    "needs_review": not confident_name,
                    "source": "scanned",
                    "last_scanned": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
                })
    return components, seen_files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", help="Path to the product repository root")
    parser.add_argument(
        "--paths", nargs="+", default=["src/components"],
        help="Directories to scan, relative to project_root",
    )
    parser.add_argument("--extensions", nargs="+", default=DEFAULT_EXTENSIONS)
    parser.add_argument("--out", default=".ui-engineering/component-catalog.json")
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    components, seen_files = scan(root, args.paths, args.extensions)
    framework = detect_framework(seen_files)

    catalog = {
        "version": "1.0",
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z"),
        "project_root": str(root),
        "scanned_paths": args.paths,
        "framework": framework,
        "components": components,
        "unresolved_references": [],
        "stats": {
            "total_components": len(components),
            "needs_review_count": sum(1 for c in components if c["needs_review"]),
        },
    }

    out_path = root / args.out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(catalog, indent=2) + "\n", encoding="utf-8")
    print(
        f"Wrote {len(components)} components "
        f"({catalog['stats']['needs_review_count']} need review) to {out_path}"
    )


if __name__ == "__main__":
    main()
