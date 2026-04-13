---
name: wiki
description: LLM-managed personal wiki. Ingest sources, query the wiki, and check health status. Subcommands: init, ingest, query, lint.
---

# Wiki

A personal wiki system written and maintained by an LLM. Uses Obsidian as the viewer.

## Usage

- `/wiki init` — Create the initial wiki structure
- `/wiki ingest <file|directory>` — Integrate sources into the wiki
- `/wiki query <question>` — Search the wiki and synthesize an answer
- `/wiki lint` — Check wiki health status

## Subcommand Parsing

Parse the first word from ARGUMENTS as the subcommand. The remainder are arguments for that operation.

| First word | File to read | Arguments |
|------------|--------------|-----------|
| `init` | `ops/init.md` | None |
| `ingest` | `ops/ingest.md` | Everything remaining (file or directory path) |
| `query` | `ops/query.md` | Everything remaining (question text) |
| `lint` | `ops/lint.md` | None |

If no subcommand is provided or it is unrecognized, display the usage above.

## Execution

1. Parse the subcommand.
2. Read the corresponding `ops/*.md` file using the Read tool.
3. Follow the instructions in the file exactly. Pass along any arguments if present.

## Wiki Location

The wiki root is the `wiki/` directory within the current working directory. If the current directory is `wiki/` itself, use the current directory as the wiki root.
