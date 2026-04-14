# Process

Process inbox/ files into reference documents. Only creates objective summaries — insights, hypotheses, and other interpretive documents are created through `/kb discuss`.

## Arguments

- **File path** (e.g. `inbox/article.md`) — single-file process
- **Directory path** (e.g. `inbox/`) — batch process all unprocessed files
- **No argument** — defaults to batch process on `inbox/`

## Prerequisites

- KB must be initialized (`index.md` must exist). If not, tell the user to run `/kb init`.
- Source files must live under `inbox/`.

---

## Single-file process

### 1. Read the source

Read the file. If it references images (`![[img.png]]` or `![](path)`), inspect those too.

### 2. Create a Reference document

Write a Reference document in `_internal/references/`:

- Structured summary of the source content
- Key points as bullet list
- Important terms or concepts mentioned
- Use the frontmatter format from CLAUDE.md

This is an objective summary. Do not inject opinions, insights, or interpretations.

### 3. Update index.md

Add a new row to the `index.md` table.

### 4. Log it

Prepend to `log.md` (right after the `# KB Log` header):

```markdown
## [YYYY-MM-DD] process | Source Title
- source: inbox/filename.md
- created: [[ref-name]]
- summary: one-line factual summary
```

### 5. Report and prompt

Summarize what was created, then suggest:

> "Run `/kb discuss [[ref-name]]` to explore this material and capture your thoughts."

---

## Batch process

### 1. Find unprocessed files

- Parse `log.md` for already-processed paths (look for `- source:` lines).
- Glob for files in the target directory (exclude hidden files and subdirectories).
- Subtract to get the unprocessed list.

### 2. Nothing to do?

If the list is empty, say "No unprocessed files in inbox/" and stop.

### 3. Show the list

Present the unprocessed files and ask: "Process all of these, or pick specific ones?"

### 4. Process each file

For each file, follow the single-file process flow above. Process sequentially to avoid write conflicts on index.md and log.md.

### 5. Summary

After all files are processed, report totals: sources processed, references created.

Suggest: "Run `/kb discuss` on any reference to start exploring."
