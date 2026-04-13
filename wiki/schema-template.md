# Wiki Schema

This is an LLM-maintained personal wiki. The LLM owns all wiki pages — creating, updating, and cross-referencing them as new sources arrive. The human curates sources, explores, and asks questions.

## Structure

- `raw/` — Source material. Immutable; the LLM never writes here.
  - `assets/` — Images
- `pages/` — Wiki pages. Flat directory, no subfolders.
- `index.md` — Page catalog with tag groupings and a master table.
- `log.md` — Append-only activity log (newest first).

## Page format

Every page in `pages/` uses this template:

```yaml
---
title: Page Title
tags: [tag1, tag2]
sources: [raw/source-file.md]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

- **title** — Must match the filename.
- **tags** — Free-form, for ad-hoc categorization.
- **sources** — Which raw sources contributed to this page.
- **created / updated** — Only bump `updated` on edits.

## Links

- Use `[[page-name]]` (Obsidian wikilinks) for all inter-page references.
- End each page with a `## Related Pages` section listing key connections.
- Link inline whenever mentioning a concept that has its own page.

## index.md format

```markdown
# Wiki Index

## By Tag
### tag-name
- [[page-name]] — one-line description

## All Pages
| Page | Tags | Sources | Last Modified |
|------|------|---------|---------------|
| [[page-name]] | tag1, tag2 | N | YYYY-MM-DD |
```

## log.md format

Newest first (prepend). Each entry: `## [YYYY-MM-DD] operation | title`.

```markdown
# Wiki Log

## [YYYY-MM-DD] ingest | Source Title
- source: raw/filename.md
- created: [[new-page]]
- updated: [[existing-page]]
- summary: one-line key takeaway
```

## Ground rules

1. Never touch anything in `raw/`.
2. Only create, edit, or delete files in `pages/`.
3. Update `index.md` whenever a page changes.
4. Log every operation in `log.md`.
5. When new information relates to existing pages, update them too.
6. When new information contradicts existing content, keep both and cite sources.
7. Cross-reference aggressively.
