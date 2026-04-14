# Init

Scaffold the KB directory structure.

## Prerequisites

Resolve the KB root path (see "KB root" in SKILL.md).

## Steps

### 1. Check for existing KB

If `index.md` already exists at the KB root with a `# KB Index` header, tell the user the KB is already set up and stop.

### 2. Create directories

```
inbox/
_internal/references/
_internal/insights/
_internal/hypotheses/
_internal/experiments/
_internal/results/
_internal/retrospectives/
_internal/notes/
pages/
```

### 3. Create index.md

```markdown
# KB Index

## By Tag

(No documents yet)

## By Type

(No documents yet)

## All Documents
| Document | Type | Tags | Status | Last Modified |
|----------|------|------|--------|---------------|
```

### 4. Create log.md

```markdown
# KB Log
```

### 5. Create CLAUDE.md

Read `schema-template.md` from this skill's directory and write it to `CLAUDE.md` at the KB root.

### 6. Done

Show the resulting structure:

```
kb/
├── inbox/
├── _internal/
│   ├── references/
│   ├── insights/
│   ├── hypotheses/
│   ├── experiments/
│   ├── results/
│   ├── retrospectives/
│   └── notes/
├── pages/
├── index.md
├── log.md
└── CLAUDE.md
```

Tell the user:
- Open `kb/` as an Obsidian vault (or add it to an existing vault) to browse the knowledge base.
- Drop raw files (articles, notes, screenshots, anything) into `inbox/`.
- Run `/kb process` to start processing them with the LLM.
