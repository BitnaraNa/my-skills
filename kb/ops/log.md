# Log

Show recent activity summary from the knowledge base log.

## Arguments

None.

## Prerequisites

KB must be initialized (`log.md` must exist).

## Steps

### 1. Read log.md

Read `log.md` in full.

### 2. Empty?

If the log has no entries (only the `# KB Log` header), say "No activity recorded yet. Run `/kb process` to get started." and stop.

### 3. Display summary

Show the last 10 entries from the log. For each entry, show:
- Date and operation type
- Title
- Key details (what was created/updated)

### 4. Stats

After the entries, show a brief stats summary:

```
---
Total: N entries
  process: N | discuss: N | capture: N | query: N | consolidate: N | lint: N
First entry: YYYY-MM-DD
Last entry: YYYY-MM-DD
```
