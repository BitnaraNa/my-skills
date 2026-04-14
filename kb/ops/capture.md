# Capture

Save a thought as a structured document in the KB. Use this outside of `/kb discuss` when the user has a standalone idea to record.

## Arguments

- **Type** (optional) — `insight`, `hypothesis`, `experiment`, `result`, `retrospective`, `note`
- Remaining text is the thought to capture

If no type is specified, ask the user what kind of thought this is.

## Prerequisites

- KB must be initialized (`index.md` must exist).

---

## Steps

### 1. Understand the thought

Read what the user provided. If it's brief or ambiguous, ask a clarifying question — but only one. Don't interrogate.

### 2. Determine the type

If the type wasn't specified, suggest one based on the content:

| Signal | Suggested type |
|--------|---------------|
| A pattern, finding, or realization | insight |
| A prediction or something testable | hypothesis |
| A plan to test something | experiment |
| An outcome from a test | result |
| A reflection on what happened | retrospective |
| Anything else | note |

Confirm with the user: "This sounds like an insight — agree?"

### 3. Find related documents

Read `index.md` to find existing documents related to this thought. If found, ask:

> "This seems related to [[existing-doc]]. Should I link them?"

### 4. Create the document

- Write the file in the appropriate `_internal/` subdirectory.
- Use the user's own words as the core content. Don't rewrite their thinking.
- Set `derived_from` / `related` links as confirmed by the user.
- Update `leads_to` on any parent documents.
- For hypotheses: confirm `expected_outcome` and set `status: proposed`.
- For experiments: confirm `method`, `success_criteria`, and link to the hypothesis.
- For results: confirm `outcome`, `verdict`, and link to the experiment.
- For retrospectives: capture `what_worked`, `what_didnt`, `what_learned` in the user's words.

### 5. Update index.md

Add the new document to:
- The "By Tag" section under each relevant tag.
- The "By Type" section under the document type.
- The "All Documents" table.

### 6. Log it

```markdown
## [YYYY-MM-DD] capture | Document Title
- type: insight|hypothesis|...
- created: [[doc-name]]
- related: [[linked-doc-1]], [[linked-doc-2]]
```

### 7. Confirm

Tell the user what was saved and where, with a `[[wikilink]]` they can follow.
