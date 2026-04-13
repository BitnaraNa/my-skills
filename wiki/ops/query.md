# Query

Answer a question using the wiki.

## Arguments

The question text (e.g. `How does X relate to Y?`).

## Prerequisites

Wiki must be initialized (`index.md` must exist).

## Steps

### 1. Scan the index

Read `index.md` to get an overview of all pages and their tags.

### 2. Find relevant pages

Match the question against page descriptions and tags. If the index isn't enough, Grep for keywords in `pages/`.

### 3. Read the pages

Read the relevant pages in full.

### 4. Synthesize

- Compose an answer drawing on the pages you read.
- Cite sources as `[[page-name]]`.
- When combining information from multiple pages, make clear what came from where.
- If pages disagree, present both sides.

### 5. Offer to save

If the answer represents a meaningful synthesis — combining multiple pages, surfacing a new connection, or producing something worth referencing again — ask:

> "Want me to save this as a wiki page?"

### 6. Save (if approved)

- Write a new page in `pages/`. Set `sources` in the frontmatter to the original raw sources of the pages you drew from.
- Add `[[wikilink]]` references from related pages to the new one.
- Update `index.md`.
- Prepend to `log.md`:

```markdown
## [YYYY-MM-DD] query | The question asked
- answer: one-line summary
- created: [[new-page-name]]
```
