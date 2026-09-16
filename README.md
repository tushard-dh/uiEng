# ui-engineering skill installer

Portable installer for the `ui-engineering` Claude Code skill (the `/uiEng`
workflow). Use this to set up the exact same skill on another machine, from
this GitHub repo, without manually copying folders around.

The skill itself lives at `ui-engineering-skill/` in this repo. This
repo root (`install.sh`, `README.md`, `COMMANDS.md`) is just the
distribution mechanism — it is not the skill itself.

Repo: https://github.com/tushardh14/uiEng

## Install on another device

Clone this repo (or just grab `install.sh`) onto the new machine, then run:

```bash
# Global install — available in every project on this machine
./install.sh https://github.com/tushardh14/uiEng.git global

# Project-only install — run from the target product repo's root
./install.sh https://github.com/tushardh14/uiEng.git project
```

Or, without cloning anything first, run it straight from the raw GitHub URL:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/tushardh14/uiEng/main/install.sh) \
  https://github.com/tushardh14/uiEng.git global
```

Optional third argument pins a branch/tag:

```bash
./install.sh https://github.com/tushardh14/uiEng.git global v1.2.0
```

## What it does

1. Shallow-clones the given repo into a temp directory.
2. Searches the clone for `SKILL.md` (up to 3 levels deep) — this makes it
   resilient to the skill folder being renamed or moved, rather than
   depending on a hardcoded path.
3. Copies that directory to:
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
