# Content Fusion Module (refresh, not rewrite)

Purpose: this is the heart of how generated improvements get MERGED into the
existing page, instead of producing a free-floating new set of content that
clashes with what's there. Based on professional "content refresh" practice
(Search Engine Journal, Surfer, Backlinko) and community consensus.

THE GOVERNING PRINCIPLE: refresh, don't rewrite.
Not everything should change. Changing too much destroys the ranking signals the
page already accumulated. Renovate the house; keep the address (URL) and the
sound walls (working headings, working keywords, ranking signals). Only change
the rooms that need it, and decorate new additions in the SAME style.

## 1. Per-element disposition (the core output of generation)

Generation does NOT output "a new page". It outputs a DECISION for each existing
element, plus any genuinely new additions. Every element gets one of:

- KEEP: still matches search intent and reads fine. Leave it untouched. Say why.
- REFRESH: keep the element but tighten/fix it (outdated fact, buried answer,
  weak wording). Minimal change, preserve voice.
- REPLACE: the element actively hurts (keyword-stuffed, AI-spam, wrong intent).
  Rewrite it.
- ADD: genuinely missing content the page needs (a real-demand question not yet
  covered, missing schema). New, but written in the page's existing voice.
- REMOVE: thin/filler/duplicate that adds nothing. State why it's safe to drop.

Output as a disposition table:
| Existing element | Disposition | What changes | Why |
|---|---|---|---|
| H2 "Driving Tips" | KEEP | nothing | still useful, on-intent |
| "Cheap..." intro | REPLACE | rewrite | keyword-stuffed + AI tells |
| (no FAQ schema) | ADD | add JSON-LD | FAQ not machine-readable |

## 2. Match the existing voice and density (the anti-clash rule)

This solves "if the existing FAQ is terse and I bolt on 130-word answers, it
clashes." Rules:
- DETECT the page's existing register first: sentence length, formality, answer
  length, whether it uses "we"/first person, how terse the FAQ answers are.
- New and refreshed content MUST match that register. If existing FAQ answers
  are 1-3 sentences, write new answers at 1-3 sentences, not 130-word blocks.
- GEO ideals (answer-first, citable) are still applied, but WITHIN the page's
  voice. Reconcile, don't override: a terse page gets terse answer-first FAQs,
  not long ones. Voice consistency beats hitting an ideal word count.
- Professional note: FAQ best practice is often 1-3 sentence direct answers
  anyway, which usually fits terse pages well. Long blocks are not required for
  citability; clarity and self-containment are.

## 3. What to preserve (don't break ranking signals)

- KEEP working keywords unless outdated/irrelevant.
- KEEP the URL/slug. Never change it for a page with history.
- KEEP headings that still match intent. Only restructure when the current order
  buries the answer or breaks hierarchy (e.g. H1 -> H3 skip).
- Existing long-tail content (local guides, driving tips, popular spots) that
  serves users and captures long-tail demand: KEEP or lightly REFRESH, do not
  delete just because it's not "core". It has SEO value.

## 4. Output contract for generation (with fusion)

For each element: its disposition (KEEP/REFRESH/REPLACE/ADD/REMOVE), the new text
where applicable (in the page's voice), and one-line reasoning. The change report
(modules/change-report.md) then diffs THIS against the audit's overview table, so
"before" values line up exactly with what the audit recorded.
