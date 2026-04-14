# Lint

Audit the knowledge base for structural and content issues.

## Prerequisites

- KB must be initialized (`index.md` must exist).
- At least one document must exist in `_internal/`. If empty, say so and stop.

## Steps

### 1. Scan everything

- Read `index.md`.
- Glob all `.md` files in `_internal/` subdirectories and `pages/`.
- Read each document (frontmatter + body).
- Read `log.md`.
- Glob all files in `inbox/`.

### 2. Check for issues

#### Orphan documents
Documents in `_internal/` with no inbound `[[wikilink]]` from other documents (index.md references don't count).

#### Broken links
`[[wikilinks]]` pointing to documents that don't exist.

#### Frontmatter problems
- Missing required fields: `title`, `type`, `tags`, `created`, `updated`.
- Type-specific required fields missing (e.g. Reference without `source_path`, Hypothesis without `status`).
- `title` doesn't match filename.

#### Stale hypotheses
Hypotheses with `status: proposed` where `created` is 30+ days ago. Flag as "still planning to test this?"

#### Stale experiments
Experiments with `status: planned` or `status: in-progress` past `due_date`.

#### Inbox backlog
Files in `inbox/` not found in any `log.md` `- source:` entry, older than 14 days.

#### Pages freshness
Documents in `_internal/` with `updated` date newer than the `updated` date of related `pages/` entries. Suggests consolidate is needed.

#### Tag hygiene
- Tags used only once (possible typos or overly specific).
- Tags in `index.md` that don't match actual document tags.

#### Content issues
- Documents making conflicting claims about the same topic.
- Concepts mentioned repeatedly across documents but lacking their own document.

#### Index sync
- Documents listed in `index.md` but missing from `_internal/` or `pages/`.
- Documents in `_internal/` or `pages/` but not listed in `index.md`.

#### Chain integrity
- `derived_from` links pointing to nonexistent documents.
- `leads_to` links not reciprocated (A leads_to B but B's derived_from doesn't include A).

### 3. Report

````markdown
## Lint Report — YYYY-MM-DD

### Orphan Documents (N)
- [[document]] — no inbound links

### Broken Links (N)
- [[missing]] ← linked from [[source]]

### Frontmatter (N)
- [[document]] — missing `status`

### Stale Hypotheses (N)
- [[hypothesis]] — proposed DD days ago, no experiment

### Stale Experiments (N)
- [[experiment]] — past due_date YYYY-MM-DD

### Inbox Backlog (N)
- inbox/file.md — unprocessed for DD days

### Pages Freshness (N)
- [[page]] — _internal/ updated YYYY-MM-DD, page last updated YYYY-MM-DD

### Tags (N)
- `possible-typo` — used once, verify intent

### Content (N)
- Conflict: [[doc-a]] says X, [[doc-b]] says Y
- Suggested document: "concept-z" appears in 3 documents but has no page

### Index Sync (N)
- In _internal/ but not in index: [[document]]

### Chain Integrity (N)
- [[doc-a]] leads_to [[doc-b]] but [[doc-b]] derived_from doesn't include [[doc-a]]
````

### 4. Fix

Offer specific fixes for each issue. Ask whether to apply them all at once or one by one.

After applying approved fixes, log it:

```markdown
## [YYYY-MM-DD] lint
- orphans: N resolved
- broken links: N resolved
- frontmatter: N fixed
- index sync: N fixed
- chain integrity: N fixed
```
