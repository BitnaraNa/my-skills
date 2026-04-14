# Consolidate

Synthesize _internal/ fragments into pages/ topic pages. Pages are the user's recall aid — organized so the user can revisit their own thinking, remember what they concluded, and trace back to the original sources when needed.

## Arguments

- **Topic name** (e.g. `marketing`) — consolidate documents related to that topic
- **No argument** — scan for topics that need consolidation

## Prerequisites

KB must be initialized (`index.md` must exist).

---

## With topic

### 1. Find related documents (2-stage reading)

**Stage 1:** Read `index.md`. Filter documents by:
- Tags matching the topic name
- Document titles or descriptions mentioning the topic
- Documents linked from other topic-matched documents

**Stage 2:** Read only the filtered documents in full (typically 5-15 documents).

### 2. Check existing page

Read `pages/` to see if a topic page already exists for this topic.

### 3. Synthesize

Compose a clean, readable topic page that:
- Preserves the user's own words and conclusions from insights, hypotheses, and retrospectives
- Organizes by subtopic, not by source
- Tells the story of the user's thinking: what they read, what they noticed, what they concluded, what they tested
- Includes the provenance chain: which hypotheses were tested, what results came back, what was learned
- Links to `_internal/` documents for details: "For full details, see [[reference-name]]"
- Links to original sources for re-reading: "Original source: [[ref-name]]"
- Lists open items: untested hypotheses, planned experiments
- Cites all contributing sources

### 4. Write the page

- Create or update `pages/{topic-name}.md` with frontmatter:

```yaml
---
title: Topic Name
tags: [tag1, tag2]
sources: [_internal/references/xxx, _internal/insights/yyy, ...]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

### 5. Update index.md and log

Update `index.md` to reflect the new or updated page.

Prepend to `log.md`:

```markdown
## [YYYY-MM-DD] consolidate | Topic Name
- synthesized: [[topic-name]]
- from: [[doc1]], [[doc2]], [[doc3]], ...
- summary: one-line description of what was consolidated
```

---

## Without topic

### 1. Scan for consolidation candidates

Read `index.md` in full. Identify:
- **Tag clusters**: tags with 3+ documents that don't have a corresponding `pages/` entry
- **Stale pages**: `pages/` entries whose `updated` date is older than related `_internal/` documents' `updated` dates
- **Orphan clusters**: groups of `_internal/` documents that link to each other but aren't reflected in any `pages/` entry

### 2. Propose candidates

Present the candidates to the user:

```
Consolidation candidates:
1. [New] "marketing" — 5 insights, 2 hypotheses, 1 result, no topic page yet
2. [Update] "psychology" — page last updated 2026-03-15, 3 new insights since then
3. [New] "conversion" — 4 documents share this tag, no topic page

Which ones should I consolidate? (all / pick numbers)
```

### 3. Process

For each selected candidate, follow the "With topic" flow above.

### 4. Summary

Report totals: pages created, pages updated, documents covered.
