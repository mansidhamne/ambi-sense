# Labeling rubric

Written **before** any response was labeled. Do not relabel a task to force cell balance.

## Task-level labels (already applied in the catalog)

A task is **ambiguous** iff the instruction plus tool schemas admit **at least two distinct, schema-valid tool-call resolutions**.

A task is **clean** iff exactly one such resolution exists.

Excluded from the primary set (different constructs):

- No applicable tool (BFCL irrelevance)
- Missing-function recovery unless the visible tools still admit ≥2 valid resolutions
- Full τ-bench dialogues after the user simulator has answered

## Response-level labels

Code the **first** agent turn only.

### Outcome

- **clarify**: The agent asks a question, states that the request is underspecified, or issues no tool call while requesting more information.
- **act**: The agent issues one or more tool calls, or the text is an unmistakable attempt to invoke a named tool with arguments.

### Silent failure (only if outcome = act)

- **none**: Every argument value is attested in the instruction, allowed-entity list, or schema.
- **invented_entity**: At least one ID-like argument (e.g. `PT-NX-####`, `ORD-####`) does not appear in those sources.
- **unknown**: Cannot decide (should be rare; leave a note).

Silent failure does **not** change the SDT cell. ACT + invented_entity on an ambiguous task is still a **miss**.

## SDT mapping (do not recode by hand)

| Task | Outcome | Cell |
|---|---|---|
| ambiguous | clarify | hit |
| ambiguous | act | miss |
| clean | clarify | false alarm |
| clean | act | correct rejection |

## Dual-pass protocol

1. Pass 1 and pass 2 must be independent raters, or the same rater after a washout with pass-1 hidden.
2. Reconcile disagreements in a third file; do not overwrite either pass.
3. Report Cohen’s κ and raw percent on the *unreconciled* pair.
4. Classifier accuracy is measured against the reconciled file.

A single author cannot produce two independent human passes. If only one rater is available, report that limitation and do not treat κ as inter-rater reliability.
