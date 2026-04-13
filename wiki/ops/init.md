# Init

Scaffold the wiki directory structure.

## Prerequisites

Resolve the wiki root path (see "Wiki root" in SKILL.md).

## Steps

### 1. Check for existing wiki

If `index.md` already exists at the wiki root, tell the user the wiki is already set up and stop.

### 2. Create directories

```
raw/
raw/assets/
pages/
```

### 3. Create index.md

```markdown
# Wiki Index

## By Tag

(No pages yet)

## All Pages
| Page | Tags | Sources | Last Modified |
|------|------|---------|---------------|
```

### 4. Create log.md

```markdown
# Wiki Log
```

### 5. Create CLAUDE.md

Read `schema-template.md` from this skill's directory and write it to `CLAUDE.md` at the wiki root.

### 6. Done

Show the resulting structure:

```
wiki/
├── raw/
│   └── assets/
├── pages/
├── index.md
├── log.md
└── CLAUDE.md
```

Tell the user:
- Open `wiki/` as an Obsidian vault to browse the wiki.
- Set **Obsidian > Settings > Files and links > Attachment folder path** to `raw/assets/`.
