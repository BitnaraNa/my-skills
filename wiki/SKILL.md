---
name: wiki
description: Personal wiki maintained by the LLM. Subcommands: init, ingest, query, lint.
---

# Wiki

A personal knowledge base that the LLM builds and maintains. You curate sources and ask questions; the LLM handles everything else — summarizing, cross-referencing, filing, and keeping the wiki consistent. Designed for use with Obsidian.

## Commands

- `/wiki init` — Scaffold the wiki directory structure
- `/wiki ingest <file|directory>` — Process sources into wiki pages
- `/wiki query <question>` — Answer questions using the wiki
- `/wiki lint` — Audit the wiki for issues

## Routing

The first word of ARGUMENTS determines the subcommand. The rest is passed as arguments.

| Subcommand | Reads | Arguments |
|------------|-------|-----------|
| `init` | `ops/init.md` | — |
| `ingest` | `ops/ingest.md` | File or directory path |
| `query` | `ops/query.md` | Question text |
| `lint` | `ops/lint.md` | — |

If no subcommand is given (or it's unrecognized), show the commands above.

## How it works

1. Parse the subcommand from ARGUMENTS.
2. Read the corresponding `ops/*.md` file.
3. Follow its instructions exactly, passing along any remaining arguments.

## Wiki root

The wiki lives at `wiki/` relative to the current working directory. If the cwd is already `wiki/`, use it directly.
