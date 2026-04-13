# Wiki Init

Creates the initial wiki structure.

## Prerequisites

- Confirm the wiki root path (see "Wiki Location" in SKILL.md).

## Procedure

### 1. Check if already initialized

If `index.md` exists in the wiki root, the wiki is already initialized.
Inform the user "The wiki is already initialized" and stop.

### 2. Create directories

Create the following directories:
- `raw/`
- `raw/assets/`
- `pages/`

### 3. Create index.md

Create `index.md` in the wiki root with the following content:

```markdown
# Wiki Index

## List by Tag

(No pages yet)

## Full List
| Page | Tags | Sources | Last Modified |
|------|------|---------|---------------|
```

### 4. Create log.md

Create `log.md` in the wiki root with the following content:

```markdown
# Wiki Log
```

### 5. Create CLAUDE.md

Read this skill's `schema-template.md` file using the Read tool, then Write its contents to `CLAUDE.md` in the wiki root.

### 6. Report completion

Show the user the created structure:

```
wiki/
├── raw/
│   └── assets/
├── pages/
├── index.md
├── log.md
└── CLAUDE.md
```

Inform the user that they can open the `wiki/` folder as a Vault in Obsidian to start using it immediately.
Instruct the user to set Obsidian Settings → Files and links → Attachment folder path to `raw/assets/`.
