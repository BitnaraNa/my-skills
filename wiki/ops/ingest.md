# Wiki Ingest

Read a source and integrate it into the wiki.

## Arguments

- File path (e.g. `raw/article.md`) → single ingest
- Directory path (e.g. `raw/`) → batch ingest
- No argument → batch ingest using `raw/` directory as default

## Prerequisites

- The wiki must be initialized (check for `index.md`). If missing, prompt the user to run `/wiki init` first.
- The target source file must exist in the `raw/` directory.

## Single Ingest

When a file path is given, process it directly in the current session.

### 1. Read Source

- Read the source file using the Read tool.
- If the source contains image references (`![[image.png]]`, `![](path)`), also inspect the images using the Read tool.

### 2. Share Key Content

Summarize the key content of the source in 3-5 lines and share it with the user. Ask if there is anything the user would like to emphasize.

### 3. Create/Update Wiki Pages

- Read `index.md` to identify the existing wiki page list.
- Identify the main concepts, entities, and insights from this source.
- For each one:
  - If a matching page exists: Read that page → integrate the new information via Edit. Add this source to the `sources` frontmatter. Update the `updated` date.
  - If no matching page exists: Write a new page in `pages/`. Follow the frontmatter format defined in CLAUDE.md (wiki schema).
- Add relevant `[[wikilink]]` cross-references to all pages.
- If new information contradicts existing content, state both and cite the sources.

### 4. Update index.md

- Reflect new/updated pages in the per-tag list section.
- Reflect new/updated pages in the full page table.
- Update the source count and last-modified date for existing entries.

### 5. Write to log.md

Prepend to the top of `log.md` (immediately after the `# Wiki Log` header) using the following format:

```markdown
## [YYYY-MM-DD] ingest | source title
- source: raw/filename.md
- created: [[new page 1]], [[new page 2]]
- updated: [[existing page 1]]
- summary: one-line summary of key content
```

### 6. Completion Report

Report a summary of created/updated pages and the key content added to each page.

## Batch Ingest

When a directory path is given, run sub-agents sequentially per file.

### 1. Collect List of Un-ingested Files

- Read `log.md` to extract the list of already-ingested source paths (parse paths from `- source:` lines).
- Collect the list of `.md` files in the target directory using Glob.
- Finalize the list of un-ingested files by excluding already-ingested ones.

### 2. If No Un-ingested Files Exist

Inform the user "There are no new sources to ingest" and exit.

### 3. Run Sub-agents Sequentially Per File

Show the list of un-ingested files to the user and begin processing.

For each file, run a sub-agent using the Agent tool:

**Agent prompt template:**

```
Perform a wiki ingest. Follow the procedure below.

## Wiki Root
{absolute path to wiki root}

## Wiki Schema
Read CLAUDE.md in the wiki root using the Read tool and follow the conventions.

## Target Source
{absolute path to source file}

## Procedure
1. Read the source file using the Read tool.
2. Read index.md using the Read tool to identify existing wiki pages.
3. Identify the main concepts, entities, and insights from the source.
4. For each one: Edit the existing page if it exists, otherwise Write a new page in pages/.
5. Add [[wikilink]] cross-references to all pages.
6. Update index.md (per-tag list + full page table).
7. Prepend the ingest record to the top of log.md.
8. Report the list of created/updated pages with a summary.
```

After each agent completes, proceed to the next file (sequential execution — prevents conflicts in index.md and log.md).

### 4. Final Completion Report

After all files are processed, report an overall summary:
- Number of sources processed
- Number of pages created
- Number of pages updated
