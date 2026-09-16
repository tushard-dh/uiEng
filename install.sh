#!/usr/bin/env bash
# Installs the "ui-engineering" Claude Code skill from a GitHub repo onto
# this machine, so /uiEng works the same way it does in the original project.
#
# Usage:
#   ./install.sh <github-repo-url> [global|project] [branch]
#
#   <github-repo-url>  Required. e.g. https://github.com/<org>/<repo>.git
#   global   (default) Install to ~/.claude/skills/ui-engineering
#            -> available in every project on this machine.
#   project             Install to ./.claude/skills/ui-engineering
#            -> available only in the current project (run from its root).
#   [branch]            Optional branch/tag/ref to clone. Defaults to the
#                       repo's default branch.
#
# One-liner (remote, without cloning this folder first):
#   bash <(curl -fsSL https://raw.githubusercontent.com/<org>/<repo>/main/ui-skill-installer/install.sh) \
#     https://github.com/<org>/<repo>.git global
#
# What it does:
#   1. Shallow-clones the repo into a temp dir.
#   2. Copies the skill directory (.claude/skills/ui-engineering, or .ui as
#      a fallback for older layouts) to the destination.
#   3. Leaves everything else in the source repo untouched.

set -euo pipefail

REPO_URL="${1:-${REPO_URL:-}}"
TARGET="${2:-${TARGET:-global}}"
REF="${3:-${REF:-}}"

# Where inside the source repo the skill package lives. Tries each in order.
CANDIDATE_PATHS=(".claude/skills/ui-engineering" ".ui")

if [ -z "$REPO_URL" ]; then
  echo "Usage: $0 <github-repo-url> [global|project] [branch]" >&2
  exit 1
fi

if [ "$TARGET" = "project" ]; then
  DEST="$(pwd)/.claude/skills/ui-engineering"
elif [ "$TARGET" = "global" ]; then
  DEST="$HOME/.claude/skills/ui-engineering"
else
  echo "Second argument must be 'global' or 'project' (got: $TARGET)" >&2
  exit 1
fi

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

echo "Cloning $REPO_URL ..."
CLONE_ARGS=(--depth 1)
if [ -n "$REF" ]; then
  CLONE_ARGS+=(--branch "$REF")
fi
git clone "${CLONE_ARGS[@]}" "$REPO_URL" "$TMP_DIR/repo"

SRC=""
for candidate in "${CANDIDATE_PATHS[@]}"; do
  if [ -f "$TMP_DIR/repo/$candidate/SKILL.md" ]; then
    SRC="$TMP_DIR/repo/$candidate"
    break
  fi
done

if [ -z "$SRC" ]; then
  echo "Could not find a SKILL.md under any of: ${CANDIDATE_PATHS[*]}" >&2
  echo "Check the repo layout or pass a different branch/ref." >&2
  exit 1
fi

mkdir -p "$(dirname "$DEST")"
if [ -d "$DEST" ]; then
  echo "Existing install found at $DEST — replacing it."
  rm -rf "$DEST"
fi
cp -R "$SRC" "$DEST"

echo ""
echo "Installed ui-engineering skill to: $DEST"
echo ""
echo "Next steps:"
echo "  1. Restart or reload Claude Code (skills are picked up on startup)."
echo "  2. cd into a product repo."
echo "  3. Run: /uiEng init"
echo "  4. Run: /uiEng discover <feature-name>"
