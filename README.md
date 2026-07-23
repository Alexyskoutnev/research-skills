# PhD Skills Library

Durable, project-independent research skills — guides distilled from real work so they
survive across projects, papers, and machines.

Each skill is a folder in Claude Code skill format (`SKILL.md` + reference files), so any
Claude Code session picks them up via the symlink at `~/.claude/skills/`.

## Skills

- **abstract-writing/** — how to write a paper abstract: three master recipes,
  sentence surgery checks, a mechanical checklist, and a fill-in-the-blank template.
  Distilled from forensic dissections of fifteen abstracts by leading ML researchers
  plus research on abstract-writing craft.
- **intro-related-writing/** — how to write the Introduction and Related Work: the
  seven-question funnel, three intro recipes, the credit-then-contrast pattern for
  positioning against rivals, and mechanical checklists. Same source dissections plus
  research on intro and related-work craft.

## Conventions

- One skill per folder; `SKILL.md` carries the frontmatter (name, description) and the
  short operating instructions; longer material lives in reference `.md` files beside it.
- Keep skills transferable: no project-specific data files, only reusable method.
- After improving a skill inside a project, copy the improvement back here and commit.

## Wiring into Claude Code

```bash
# from the root of this repo:
mkdir -p ~/.claude/skills
ln -sfn "$(pwd)/abstract-writing" ~/.claude/skills/abstract-writing
```
