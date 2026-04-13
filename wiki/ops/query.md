# Wiki Query

Search the wiki and synthesize an answer.

## Arguments

- Question text (e.g. `What is the difference between LLM wiki and RAG?`)

## Prerequisites

- The wiki must be initialized (verify that `index.md` exists).

## Procedure

### 1. Read index.md

Use the Read tool to read `index.md` and understand the full list of wiki pages and their tags.

### 2. Identify Relevant Pages

Identify pages related to the question based on the descriptions and tags in index.md. If needed, use the Grep tool to search for keywords in the `pages/` directory.

### 3. Read Relevant Pages

Use the Read tool to read the identified relevant pages.

### 4. Synthesize the Answer

- Compile the content from the read pages to compose an answer.
- Cite the source pages in the answer using the `[[page name]]` format.
- When synthesizing information from multiple pages, specify which information came from which page.
- If there are contradictions between pages, present both sides.

### 5. Propose Wiki Inclusion

If the answer satisfies any of the following conditions, propose to the user whether to add it to the wiki:
- A new analysis or comparison synthesizing multiple pages
- A perspective or connection that did not previously exist
- Content likely to be referenced repeatedly

Proposal format: "Would you like to save this analysis as a wiki page?"

### 6. Wiki Inclusion (upon user approval)

- Write the new page to `pages/`. Include the original sources of referenced wiki pages in the frontmatter `sources` field.
- Add a `[[wikilink]]` to the new page in related pages.
- Update `index.md`.
- Prepend the query record to `log.md`:

```markdown
## [YYYY-MM-DD] query | question content
- One-line summary of the answer
- Created: [[new page name]]
```
