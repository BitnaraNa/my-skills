# Query

Answer a question using the knowledge base.

## Arguments

The question text (e.g. `How does X relate to Y?`).

## Prerequisites

KB must be initialized (`index.md` must exist).

## Steps

### 1. Determine query mode

Based on the question, determine which mode fits best:

- **Knowledge view** — "What do I know about X?" → synthesize current understanding
- **Evolution view** — "How has my thinking about X changed?" → trace temporal chain via log.md and document dates
- **Action view** — "What's untested about X?" → filter hypotheses (status: proposed), experiments (status: planned)

Most questions are knowledge view. Only use the others when the question explicitly asks about evolution or open items.

### 2. Find relevant documents (2-stage reading)

**Stage 1:** Read `index.md` to get an overview of all documents and their tags/types. Match the question against document descriptions and tags.

**Stage 2:** If the index isn't enough, Grep for keywords in `pages/` first (synthesized content is richer), then `_internal/` if needed.

Never search `inbox/`.

### 3. Read the documents

Read the relevant documents in full. For knowledge view, prioritize `pages/` (already synthesized). For evolution/action views, read `_internal/` documents directly.

### 4. Synthesize

- Compose an answer drawing on the documents you read.
- Cite sources as `[[document-name]]`.
- When combining information from multiple documents, make clear what came from where.
- If documents disagree, present both sides with their sources.
- For evolution view, present chronologically.
- For action view, present as a checklist of open items.

### 5. Offer to save

If the answer represents a meaningful synthesis — combining multiple documents, surfacing a new connection, or producing something worth referencing again — ask:

> "Want me to save this as a page in pages/?"

### 6. Save (if approved)

- Write a new page in `pages/`. Set a simple frontmatter:

```yaml
---
title: Page Title
tags: [tag1, tag2]
sources: [_internal/insights/xxx, _internal/references/yyy]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

- Add `[[wikilink]]` references from related documents to the new page.
- Update `index.md`.
- Prepend to `log.md`:

```markdown
## [YYYY-MM-DD] query | The question asked
- answer: one-line summary
- created: [[new-page-name]]
```
