# Ingest

Process a source into wiki pages.

## Arguments

- **File path** (e.g. `raw/article.md`) — single-file ingest
- **Directory path** (e.g. `raw/`) — batch ingest all un-ingested files
- **No argument** — defaults to batch ingest on `raw/`

## Prerequisites

- Wiki must be initialized (`index.md` must exist). If not, tell the user to run `/wiki init`.
- Source files must live under `raw/`.

---

## Single-file ingest

Process one source in the current session.

### 1. Read the source

Read the file. If it references images (`![[img.png]]` or `![](path)`), inspect those too.

### 2. Discuss with the user

Share a 3-5 line summary of what's in the source. Ask if there's anything they want to emphasize or deprioritize.

### 3. Create or update pages

- Read `index.md` to see what pages already exist.
- Identify the key concepts, entities, and insights in the source.
- For each:
  - **Existing page** — Read it, integrate the new information, add this source to `sources`, bump `updated`.
  - **New topic** — Create a page in `pages/` following the format in CLAUDE.md.
- Add `[[wikilink]]` cross-references across all affected pages.
- If the new information contradicts something already in the wiki, keep both claims and cite sources.

### 4. Update index.md

Reflect all new and modified pages in both the tag list and the master table.

### 5. Log it

Prepend to `log.md` (right after the `# Wiki Log` header):

```markdown
## [YYYY-MM-DD] ingest | Source Title
- source: raw/filename.md
- created: [[new-page-1]], [[new-page-2]]
- updated: [[existing-page]]
- summary: one-line key takeaway
```

### 6. Report

Summarize what was created/updated and the key information added.

---

## Batch ingest

Process multiple sources, one sub-agent per file.

### 1. Find un-ingested files

- Parse `log.md` for already-ingested paths (look for `- source:` lines).
- Glob for `.md` files in the target directory.
- Subtract to get the un-ingested list.

### 2. Nothing to do?

If the list is empty, say so and stop.

### 3. Process each file

Show the user the list, then for each file spawn a sub-agent via the Agent tool:

**Prompt template:**

```
Perform a wiki ingest. Follow these steps exactly.

## Wiki root
{absolute path}

## Schema
Read CLAUDE.md at the wiki root and follow its conventions.

## Source
{absolute path to source file}

## Steps
1. Read the source file.
2. Read index.md to see existing pages.
3. Identify key concepts, entities, and insights.
4. For each: edit existing pages or create new ones in pages/.
5. Add [[wikilink]] cross-references.
6. Update index.md (tag list + master table).
7. Prepend an ingest entry to log.md.
8. Report what you created/updated with a brief summary.
```

Wait for each agent to finish before starting the next (sequential — avoids write conflicts on index.md and log.md).

### 4. Summary

After all files are processed, report totals: sources processed, pages created, pages updated.
