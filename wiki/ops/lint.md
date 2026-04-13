# Wiki Lint

Checks the health status of the wiki.

## Prerequisites

- The wiki must be initialized (`index.md` must exist).
- There must be at least 1 page in the `pages/` directory. If none exist, inform the user: "There are no pages in the wiki yet."

## Procedure

### 1. Full Wiki Scan

- Collect a list of all `.md` files in the `pages/` directory using Glob.
- Read each page with the Read tool to parse the frontmatter and body.
- Read `index.md`.

### 2. Check Items

Check the following items and collect results:

#### Orphan Pages
- Find pages that are not referenced by any `[[wikilink]]` from other pages.
- Exclude references from index.md (since index is a catalog).

#### Broken Links
- Find cases where `[[a non-existent page]]` is referenced in the body.
- If the corresponding file does not exist in the `pages/` directory, it is a broken link.

#### Frontmatter Check
- Confirm missing required fields (`title`, `tags`, `sources`, `created`, `updated`).
- Confirm mismatches between `title` and filename.

#### Tag Check
- List tags used only once (possible typos).
- Confirm mismatches between the per-tag list in index.md and the actual page tags.

#### Content Check
- Check whether any pages make conflicting claims about the same topic.
- Identify concepts repeatedly mentioned across multiple pages but without their own page.

#### index.md Sync
- Items in index.md but not in pages/ (deleted pages).
- Items in pages/ but not in index.md (missing registrations).

### 3. Report

Organize and report the check results by category:

````markdown
## Wiki Lint Results

### Orphan Pages (N items)
- [[page-name]] — no inbound links

### Broken Links (N items)
- [[non-existent page]] ← [[referencing page]]

### Frontmatter Issues (N items)
- [[page-name]] — `tags` field missing

### Tag Issues (N items)
- `typo-tag` — used 1 time (verify if intentional)

### Content Issues (N items)
- Contradiction: [[PageA]] says X but [[PageB]] says Y
- Page suggestion: "ConceptZ" is mentioned in 3 pages but has no page of its own

### index.md Sync (N items)
- In pages/ but not in index: [[page-name]]
````

### 4. Fix Suggestions

Provide specific fix suggestions for each issue. Ask the user whether to apply all at once or item by item.

After applying fixes approved by the user, record them in `log.md`:

````markdown
## [YYYY-MM-DD] lint
- Orphan pages: N resolved
- Broken links: N resolved
- Frontmatter fixes: N
- Index sync: N
````
