# Discuss

Have a conversation about a reference to help the user think deeply and capture their own insights, hypotheses, and notes.

## Arguments

- **Document name** (e.g. `[[ref-name]]` or `ref-name`) — discuss a specific reference
- **No argument** — show recent undiscussed references and let the user pick

## Prerequisites

- KB must be initialized (`index.md` must exist).
- At least one Reference must exist in `_internal/references/`.

---

## With document

### 1. Load context

Read the specified Reference document in full. Also read any documents already linked from it (`leads_to`).

### 2. Present the material

Give a concise overview of the reference:
- What the source covers
- Key points worth thinking about

Then begin the conversation with an open question. Examples:
- "What stands out to you here?"
- "Is there anything here that surprised you or challenged what you already knew?"
- "How does this relate to what you're working on?"

### 3. Facilitate thinking

This is a conversation, not a quiz. Follow the user's lead. Your role:

**Do:**
- Ask follow-up questions that help the user articulate their thinking
- Surface connections to other documents in the KB when relevant ("This reminds me of [[other-doc]] — do you see a connection?")
- Help the user sharpen vague thoughts into clear statements
- Challenge assumptions gently ("What would need to be true for that to work?")
- Offer the user a different angle if they're stuck ("Another way to look at this might be...")

**Don't:**
- State your own insights and ask for confirmation
- Lead the user toward a predetermined conclusion
- Rush to capture — let the conversation breathe
- Dump multiple questions at once

### 4. Capture moments

When the user says something that sounds like a distinct thought — an insight, a hypothesis, an observation — offer to capture it:

> "That sounds like an insight worth keeping: '[user's idea in their words]'. Want me to save it?"

If the user agrees, create the document immediately:
- Write it in the appropriate `_internal/` subdirectory
- Use the user's own language as the core of the document
- Set `derived_from` to link back to the reference (and any other sources discussed)
- Update `leads_to` on the parent reference
- Update `index.md`

For hypotheses specifically, always confirm:
> "Should I frame this as a hypothesis? What outcome would you expect?"

Then set `status: proposed` and record their expected outcome.

### 5. Wrap up

When the conversation winds down naturally (or the user signals they're done), summarize what was captured:

```
Captured from this discussion:
- [Insight] "user's insight title"
- [Hypothesis] "user's hypothesis title" (status: proposed)

The reference [[ref-name]] now links to these.
```

Log the discussion:

```markdown
## [YYYY-MM-DD] discuss | Reference Title
- reference: [[ref-name]]
- captured: [[insight-1]], [[hypothesis-1]]
- summary: one-line description of what was explored
```

If nothing was captured, that's fine too — not every discussion needs to produce artifacts.

---

## Without document

### 1. Find undiscussed references

Read `index.md` to get all References. Read `log.md` to find which references have had a `discuss` entry. Show references that haven't been discussed yet.

### 2. Present options

```
References you haven't explored yet:
1. [[ref-name-1]] — one-line description
2. [[ref-name-2]] — one-line description
3. [[ref-name-3]] — one-line description

Pick one to discuss, or I can suggest which might be most interesting.
```

### 3. Proceed

Once the user picks, follow the "With document" flow.
