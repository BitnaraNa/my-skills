# Lint

Audit the wiki for structural and content issues.

## Prerequisites

- Wiki must be initialized (`index.md` must exist).
- At least one page must exist in `pages/`. If empty, say so and stop.

## Steps

### 1. Scan everything

- Glob all `.md` files in `pages/`.
- Read each page (frontmatter + body).
- Read `index.md`.

### 2. Check for issues

#### Orphan pages
Pages with no inbound `[[wikilink]]` from other pages (index.md references don't count — it's a catalog, not a real link).

#### Broken links
`[[wikilinks]]` pointing to pages that don't exist in `pages/`.

#### Frontmatter problems
- Missing required fields: `title`, `tags`, `sources`, `created`, `updated`.
- `title` doesn't match filename.

#### Tag hygiene
- Tags used only once (possible typos).
- Tags in index.md that don't match actual page tags.

#### Content issues
- Pages making conflicting claims about the same topic.
- Concepts mentioned repeatedly across pages but without their own page.

#### Index out of sync
- Pages listed in index.md but missing from `pages/`.
- Pages in `pages/` but not listed in index.md.

### 3. Report

````markdown
## Lint Report

### Orphan Pages (N)
- [[page]] — no inbound links

### Broken Links (N)
- [[missing-page]] <- [[linking-page]]

### Frontmatter (N)
- [[page]] — missing `tags`

### Tags (N)
- `possible-typo` — used once, verify intent

### Content (N)
- Conflict: [[page-a]] says X, [[page-b]] says Y
- Suggested page: "concept-z" appears in 3 pages but has no page

### Index Sync (N)
- In pages/ but not in index: [[page]]
````

### 4. Fix

Offer specific fixes for each issue. Ask whether to apply them all at once or one by one.

After applying approved fixes, log it:

````markdown
## [YYYY-MM-DD] lint
- orphan pages: N resolved
- broken links: N resolved
- frontmatter: N fixed
- index sync: N fixed
````
