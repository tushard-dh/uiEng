# ui-engineering skill installer

Portable installer for the `ui-engineering` Claude Code skill (the `/uiEng`
workflow). Use this to set up the exact same skill on another machine from
a GitHub repo, without manually copying folders around.

The skill itself lives at `.claude/skills/ui-engineering/` in this repo
(source package: `.ui/`). This `ui-skill-installer/` folder is just the
distribution mechanism — it does not contain the skill itself.

## Prerequisite: push this repo to GitHub

This installer clones a repo URL, so the repo needs to be on GitHub first:

```bash
git remote add origin https://github.com/<org>/<repo>.git
git push -u origin main
```

(Skip this if the repo is already pushed.)

## Install on another device

Clone this repo (or just this script) onto the new machine, then run:

```bash
# Global install — available in every project on this machine
./install.sh https://github.com/<org>/<repo>.git global

# Project-only install — run from the target project's root
./install.sh https://github.com/<org>/<repo>.git project
```

Or, without cloning anything first, run it straight from the raw GitHub URL:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/<org>/<repo>/main/ui-skill-installer/install.sh) \
  https://github.com/<org>/<repo>.git global
```

Optional third argument pins a branch/tag:

```bash
./install.sh https://github.com/<org>/<repo>.git global v1.2.0
```

## What it does

1. Shallow-clones the given repo into a temp directory.
2. Looks for the skill package at `.claude/skills/ui-engineering/` (falls
   back to `.ui/` for older layouts) and confirms `SKILL.md` is present.
3. Copies it to:
   - `~/.claude/skills/ui-engineering` for a `global` install, or
   - `./.claude/skills/ui-engineering` for a `project` install.
4. Cleans up the temp clone.

## After installing

1. Restart/reload Claude Code so it picks up the new skill.
2. In a product repo: `/uiEng init`
3. See `COMMANDS.md` in this folder for the full command reference.

## Updating an existing install

Re-run the same install command — it replaces the destination folder with
the latest clone. Project-local `.ui-engineering/` state (decisions, specs,
knowledge) is untouched since it lives outside the skill directory.
