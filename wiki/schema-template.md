# Wiki Schema

This directory is an LLM-managed personal wiki. The LLM writes and maintains all wiki pages. The user focuses on source curation, navigation, and asking questions.

## Directory Structure

- `raw/` — Original sources. Immutable. The LLM only reads from here.
  - `assets/` — Image files
- `pages/` — Wiki pages owned by the LLM. Flat structure.
- `index.md` — Full wiki catalog.
- `log.md` — Chronological activity log.

## Page Format

All wiki pages (`pages/*.md`) follow this format:

```yaml
---
title: Page Title
tags: [tag1, tag2]
sources: [raw/source-file.md]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

- **title**: Matches the filename.
- **tags**: Free-form. Used for post-hoc categorization.
- **sources**: List of original source paths that contributed to this page.
- **created**: Date first created.
- **updated**: Date last modified.

## Link Conventions

- References between wiki pages use the `[[page-name]]` format (Obsidian wikilink).
- Key connections are listed in a `## Related Pages` section at the bottom of each page.
- Use `[[wikilink]]` inline in body text when mentioning related concepts.

## index.md Format

```markdown
# Wiki Index

## By Tag
### tag-name
- [[page-name]] — one-line description

## All Pages
| Page | Tags | Sources | Last Modified |
|--------|------|---------|-----------|
| [[page-name]] | tag1, tag2 | N | YYYY-MM-DD |
```

## log.md Format

Latest entry at the top (prepend). Each entry uses the format `## [YYYY-MM-DD] operation | title`.

```markdown
# Wiki Log

## [YYYY-MM-DD] ingest | Source Title
- source: raw/filename.md
- created: [[new page]]
- updated: [[existing page]]
- summary: one-line summary of key content
```

## Rules

1. Never modify files in the `raw/` directory.
2. Only create, modify, or delete files in the `pages/` directory.
3. Update `index.md` every time a page is created or modified.
4. Log all activity in `log.md`.
5. If new information relates to an existing page, update that page as well.
6. If new information contradicts existing content, state both explicitly and indicate which source each piece of information comes from.
7. Actively add cross-references between pages.
