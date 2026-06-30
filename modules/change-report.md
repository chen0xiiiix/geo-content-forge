# Change Report Module

Purpose: after generating new content, tell the user EXACTLY what changed versus
the current live page, element by element, classified as NEW / REWRITTEN /
REMOVED / UNCHANGED, plus a HONEST, qualitative statement of expected effect.
Runs last (after generation + both gates).

Inputs: the Stage-1 audit OVERVIEW TABLE (the "before" = actual recorded
values) and the fusion dispositions (the "after"). The change report MUST pull
"before" values directly from the audit overview table so they line up exactly,
never re-derive or guess them. Map fusion dispositions: KEEP=UNCHANGED,
REFRESH/REPLACE=REWRITTEN, ADD=NEW, REMOVE=REMOVED.

---

## 1. Element-by-element diff

For each element, state old -> new and classify:

| Element        | Before (from audit)        | After (generated)         | Change type |
|----------------|----------------------------|---------------------------|-------------|
| Title          | old title (chars)          | new title (chars)         | REWRITTEN   |
| Meta           | old meta (chars)           | new meta (chars)          | REWRITTEN   |
| H1             | old H1                     | new H1                    | NEW/REWRITTEN |
| H2 (each)      | old or "(none)"            | new                       | NEW/REWRITTEN/REMOVED |
| FAQ (each Q)   | old or "(none)"            | new                       | NEW/REWRITTEN |
| Schema         | present? type              | FAQPage JSON-LD added     | NEW/UNCHANGED |

Classification rules:
- NEW: element/section did not exist before.
- REWRITTEN: existed, content changed. Show what specifically changed (e.g.
  "added off-hour fee detail; removed vague 'convenient pickup' line").
- REMOVED: existed before, intentionally dropped. STATE WHY (e.g. violated a
  constraint, was placeholder, was thin/duplicate).
- UNCHANGED: kept as-is (and say why it was fine).

## 2. Why each change (tie to evidence)

For meaningful changes, give the reason, drawn from real inputs:
- Constraint-driven ("removed X because constraint brief forbids it")
- Gap-driven ("added this FAQ because it's real demand competitors cover thinly"
 , cite the keyword/competitor evidence)
- Voice-driven ("rewrote to remove AI tells: em dash, 'seamless', metronome")
- Citability-driven ("restructured to answer-first, ~150 words, self-contained")

## 3. Expected effect (QUALITATIVE only, never promise numbers)

State plainly what the changes are designed to improve, and be honest about
uncertainty and timeframe:
- What this should help: e.g. "answer-first FAQ blocks with concrete figures are
  the format AI search tends to cite; off-hour fee + exact Door/time details fill
  a gap competitors leave vague."
- Honest limits: "This does not guarantee ranking or citation. On-page changes
  typically show gradual effect over ~30-90 days, influenced by competition,
  crawl frequency, and overall site authority, factors outside this page."
- What to measure: suggest tracking impressions/clicks for the target queries in
  Google Search Console, and watching whether the page starts appearing in AI
  answers, as the real feedback loop.
- NEVER state a predicted % lift, traffic number, or ranking position. If asked
  for those, explain they require historical data + tools and are still estimates.

## 4. Output format, be DIRECT, lead with the bottom line

Don't bury the point. Structure it so the user instantly sees what changed and
whether it matters:

LINE 1 - the bottom line, one sentence:
  "5 changes: rewrote the keyword-stuffed intro into 3 question-led sections,
   added FAQ schema, added an after-hours-cost FAQ competitors don't answer
   clearly. Net: more extractable by AI search, no constraint risk."

THEN - the change table (section 1), tight: Element | Before | After | Type.
  One row per element. No prose padding inside cells.

THEN - "Why it matters", only for the changes that matter, one line each:
  "Intro rewrite: removed keyword stuffing (a quality/AI-spam signal) and made
   each section answer-first, which is the format AI search extracts."

THEN - "Expected effect", 2-3 sentences, honest:
  what it's designed to improve + the honest limit (no guaranteed ranking;
  ~30-90 days; depends on competition and site authority) + what to track in GSC.

THEN - counts: "X new, Y rewritten, Z removed, W flagged for your decision."

Tone: direct and factual, not salesy. A busy client should get the whole story
from LINE 1 alone, and detail below only if they want it. Never inflate results,
never predict a number.
