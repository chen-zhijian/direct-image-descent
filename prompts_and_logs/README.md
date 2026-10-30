# Provenance records

This directory contains a partial recovery of local research records, collected on October 24, 2026 with the author's authorization.

These records are preserved for historical provenance from the first-version and predecessor work. The current paper is [paper v2](../papers/paper_v2.pdf), based on [direct_image_descent.tex](../papers/src/direct_image_descent.tex), dated October 30, 2026. This directory does not contain a recovered development transcript or review record for that revision. Its earlier titles, scope descriptions, and mathematical judgments may therefore differ from or be superseded by v2. The archived [first-version source](../papers/src/main.tex) and [PDF](../papers/paper_v1.pdf) remain available unchanged.

## Selected visible conversation

[conversation.json](conversation.json) exports 58 original user-visible messages from the ten most recent turns of the Codex chat titled “Summarize the past works on the positivity of direct image…”. The selected turns run from October 23 to October 24, 2026 and cover the general variation discussion, development of the predecessor draft, creation of the two-theorem article, referee-style revisions, and the nonsplit-metric and fibration extensions.

The export preserves ten user messages, 38 assistant commentary messages, and ten final answers in chronological turn order. User-selected quotations from an earlier answer are retained separately. It copies the returned message text with documented transformations: absolute local paths become `[local path omitted]`; platform attachment and annotation wrappers and internal citation directives are removed; outer whitespace is trimmed. Ordinary public web links and mathematical prose are retained. This is a redacted selection, not an unmodified full transcript or a retrospective summary.

The retrieval used `read_thread` with ten turns, a 20,000-character per-item limit, and tool outputs disabled. No selected message reaches that character limit; the tool provides no per-item truncation flag. Older turns remain available outside the selected page, so the export explicitly records incomplete coverage. Historical claims of successful checking, earlier errors, and superseded approaches retain their original context and are not endorsements of correctness or novelty.

Hidden reasoning, reasoning summaries, system/developer instructions, tool calls and outputs, and subagent/internal activity are excluded. No failed attempt has been reconstructed; only relevant statements actually visible within the selected turns are retained.

## Research and review notes

[review_notes/](review_notes/README.md) contains five byte-for-byte copies of the local synopsis and review/extension notes as recovered on October 24, 2026. Their file hashes and source modification timestamps are recorded in [review_notes/manifest.json](review_notes/manifest.json). These documents refer to different historical manuscript stages; “referee” and “independent check” describe the research workflow and do not establish external journal peer review or review of v2.

## Remaining gaps

- `system_prompt.txt` is an availability notice. The original research system prompt has not been supplied and is not reconstructed.
- The selected conversation establishes use of Codex, but does not establish a precise model, provider/version configuration, or complete record of AI assistance.
- `cost_summary.md` records unavailable token, compute, and billing data. Unknown values are not zero.
- Older turns, any other original exports, and any unavailable failed attempts are outside this partial recovery.
- No Lean formalization or other machine-checked proof is supplied.

Any later additions should identify their original source and dates, distinguish copied messages from later summaries, and preserve the distinction between manuscript-development work and repository preparation.
