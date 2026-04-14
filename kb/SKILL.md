---
name: kb
description: LLM-managed knowledge base. Subcommands: init, process, discuss, capture, query, lint, consolidate, log.
---

# KB

A personal knowledge base that the LLM organizes and the user thinks through. You curate sources; the LLM summarizes and files them. You explore and think; the LLM facilitates discussion and captures your conclusions. Designed for use with Obsidian.

Three layers:
- **inbox/** — You drop raw files here. The LLM reads but never modifies.
- **_internal/** — Structured documents. References are created by the LLM; insights, hypotheses, and other interpretive documents are created through conversation with you.
- **pages/** — Synthesized pages for you to read. The LLM generates these from _internal/.

Core workflow:
1. Drop sources into `inbox/`
2. `/kb process` — LLM creates objective reference summaries
3. `/kb discuss` — You explore the material in conversation, capture your own insights and hypotheses
4. `/kb capture` — Record a standalone thought anytime
5. `/kb consolidate` — Synthesize everything into readable topic pages

## Commands

- `/kb init` — Scaffold the KB directory structure
- `/kb process [file|dir]` — Process inbox files into reference summaries
- `/kb discuss [ref]` — Explore a reference in conversation; capture insights and hypotheses
- `/kb capture [type] <thought>` — Save a standalone thought as a structured document
- `/kb query <question>` — Answer questions using the knowledge base
- `/kb lint` — Audit the KB for issues
- `/kb consolidate [topic]` — Synthesize _internal/ fragments into pages/
- `/kb log` — Show recent activity summary

## Routing

The first word of ARGUMENTS determines the subcommand. The rest is passed as arguments.

| Subcommand | Reads | Arguments |
|------------|-------|-----------|
| `init` | `ops/init.md` | — |
| `process` | `ops/process.md` | File or directory path (optional) |
| `discuss` | `ops/discuss.md` | Document name (optional) |
| `capture` | `ops/capture.md` | Type (optional) + thought text |
| `query` | `ops/query.md` | Question text |
| `lint` | `ops/lint.md` | — |
| `consolidate` | `ops/consolidate.md` | Topic name (optional) |
| `log` | `ops/log.md` | — |

If no subcommand is given (or it's unrecognized), show the commands above.

## How it works

1. Parse the subcommand from ARGUMENTS.
2. Read the corresponding `ops/*.md` file.
3. Follow its instructions exactly, passing along any remaining arguments.

## KB root

The KB lives at `kb/` relative to the current working directory. If the cwd already contains `index.md` with a `# KB Index` header, use the cwd directly.
