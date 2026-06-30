# Page Audit Report Module

Purpose: produce a professional on-page SEO audit of the TARGET page before any
content is written. This is the "x-ray" step: it records what the page currently
is, so generation has a baseline and the change report (later) can diff against
it. Everything here is Measured (read from the fetched page). Never infer.

Run this in Part 0.1 (right after fetching the page).

STRUCTURE DATA SOURCE: get the heading tree and tags via
modules/structure-extraction.md (Tier 1 script -> Tier 2 user's Ahrefs/export ->
Tier 3 lossy fallback). List EVERY level H1-H6 in the overview; if a level is
absent write "none found"; if levels couldn't be verified at the current tier,
say so explicitly. Never silently omit H4-H6.

NOTE: do not tag rows by who executes them; all fixes go to the developer/IT to
implement. The only special case is a fact that IT cannot know , e.g. the real
opening hours when the page contradicts itself. Mark those rows "needs confirm"
so someone checks the true value before IT applies it.

---

## 1. Structural inventory (extract verbatim from the page)

Record, exactly as they appear:
- Title tag + character count (flag if outside 50-60 chars)
- Meta description + character count (flag if outside 150-160 chars; note it
  affects CTR, not ranking directly)
- URL (flag if not lowercase-hyphenated, or >75 chars)
- Canonical tag (present? self-referential?)
- H1: list every H1 found. FLAG if zero or more than one (exactly one required).
- Full heading tree H1->H2->H3->H4->H5->H6 in document order.
  FLAG any skipped level (H1 then H3 with no H2 = broken hierarchy).
  FLAG empty heading tags (a heading element with no text).
- Existing structured data / schema types present (FAQPage, LocalBusiness, etc.)
- Image alt text: count images, count missing/empty alt
- Internal links count, external links count
- Word count (FLAG if under ~400 words for a page targeting competitive terms)

## 2. Heading-quality check (against professional standards)

For each heading judge, don't just list:
- Is the single H1 descriptive and does it carry the primary topic? (H1 should
  differ from the title tag but cover the same topic.)
- Are H2s real section titles (or real questions), not decorative phrases?
- Are H3s nested under a relevant H2 (e.g. FAQ items as H3 under an "FAQ" H2)?
- Any heading clearly tied to nav labels rather than content? FLAG it.
- Any keyword-stuffed headings? FLAG.

## 3. Keyword classification (from the page's own text)

Analyze the body text and classify the terms the page currently targets:
- HEAD terms (short, high-level: e.g. "car rental auckland")
- LONG-TAIL (specific multi-word: e.g. "12-seater van hire auckland airport")
- QUESTION phrasings present (or absent)
- SEMANTIC / related terms actually used
- Primary keyword: does it appear in title, H1, first 100 words? (check each)
- Obvious keyword stuffing or repetition? FLAG.
- Cannibalization risk: does this page target the same head term as another of
  the site's pages? (note if detectable; full check needs a crawl)
Tie the classification back to the real opportunity list from the Keyword
Intelligence module (Tier 1+). Mark which in-demand terms the page already
covers and which it misses.

## 4. Issues list, prioritized

Group findings by impact (standard audit tiering):
- HIGH: missing/duplicate H1, broken canonical, noindex on a page meant to rank,
  empty headings, placeholder text live (e.g. Lorem Ipsum), thin content
- MEDIUM: title/meta length or duplication, weak/decorative H2s, missing schema,
  missing alt text, primary keyword absent from H1/first 100 words
- LOW: microcopy, minor phrasing, nice-to-have semantic additions

## 5. Output format (clean, bulleted, complete)

Formatting rules (apply to the whole report):
- Use clear bullet points, one idea per line. Never pack many facts into one
  run-on line separated by punctuation.
- No em dashes anywhere (the skill's own voice rule applies to its reports too).
- Lead with the verdict, then the complete overview, then priorities, then detail.

### 5.1 Health verdict (one line)
A single sentence: overall state + how many HIGH issues.

### 5.2 COMPLETE PAGE OVERVIEW (the master table, list every element with its
actual value)

This is the table the user asked for: every on-page element, its ACTUAL current
value read from the page, whether it has a problem, the risk level, and the fix.
Never omit base elements like title/meta/H1 just because they pass; show them all.

| Element | Current value (actual, from page) | Issue? | Risk | How to fix |
|---|---|---|---|---|
| Title | (the real title text + char count) | yes/no | High/Med/Low/- | (fix or "-") |
| Meta description | (real text + char count) | ... | ... | ... |
| URL / slug | (real URL) | ... | ... | ... |
| Canonical | (actual value, e.g. unresolved :slug) | ... | ... | ... |
| H1 | (actual H1 text; count if !=1) | ... | ... | ... |
| H2s | (list actual H2s, or "none found") | ... | ... | ... |
| H3s | (list actual H3s, or "none found") | ... | ... | ... |
| H4s | (list actual H4s, or "none found") | ... | ... | ... |
| H5s | (list actual H5s, or "none found") | ... | ... | ... |
| H6s | (list actual H6s, or "none found") | ... | ... | ... |
| Heading hierarchy | (e.g. "H1 -> H3, skips H2") | ... | ... | ... |
| Schema present | (actual types, or none) | ... | ... | ... |
| Open Graph tags | (present/empty) | ... | ... | ... |
| Word count | (number) | ... | ... | ... |
| Images / alt | (count, missing alt count, wrong alt) | ... | ... | ... |
| Internal links | (count) | ... | ... | ... |
| Freshness signal | (last-updated present? date?) | ... | ... | ... |

Every row shows the REAL value (Measured). The "Issue?/Risk/How to fix" columns
make the whole health picture scannable in one table.

### 5.3 Prioritized issues , ONE single table, sorted by level
All issues in a SINGLE table with a Level column (do not split into separate
HIGH/MEDIUM/LOW tables). Sort High first, then Medium, then Low.

| Level | Problem | Fix | Needs confirm? |
|---|---|---|---|
| High | canonical is :slug template var | set self-referential canonical | - |
| High | opening hours conflict (8-17 vs 8-18) | unify to the true value | yes (ask owner) |
| Medium | "cheap" stuffing in intro | rewrite as Q-led | - |
| Low | no last-updated signal | add updated date | - |

The "Needs confirm?" column flags rows where IT can't know the true value and a
person must confirm it first.

### 5.4 Keyword classification (own table)
| Type | Terms found on page | Where it appears | In-demand but MISSING |
|---|---|---|---|
| Head | ... | title/H1/first-100 | ... |
| Long-tail | ... | ... | ... |
| Question | ... | ... | ... |
| Semantic | ... | ... | ... |
Plus a keyword-stuffing flag with the stuffed passage quoted.

## 6. Scope boundary, what single-page analysis CAN'T see (state clearly, don't dump a cryptic "needs crawl")

Some checks are physically impossible from one fetched page. When you hit one,
explain WHY and HOW to get it, in plain words, never just flag "needs crawl":

- KEYWORD CANNIBALIZATION (do other pages on this site target the same term?):
  requires fetching the whole site, not one page. Say: "To check whether other
  pages compete for this keyword, a full-site crawl is needed (e.g. Screaming
  Frog), or fetch the other key pages too. Single-page analysis can't see this."
  OPTIONAL PARTIAL CHECK: if the nav exposes sibling pages (e.g. other location
  pages), you MAY fetch a few and do a partial cannibalization check, note it's
  partial, not a full-site audit.
- INDEXATION / IMPRESSIONS / CLICKS (is the page actually indexed? how does it
  perform?): this data lives ONLY in Google Search Console, the site owner's
  private account. Say: "Indexation and performance data require Google Search
  Console access (BYOK). It can't be read by fetching the page from outside."
- BACKLINKS / DOMAIN AUTHORITY: requires a backlink database (Ahrefs/Semrush).
  Say so; mark N/A without a key.

Rule: every boundary line tells the user WHAT can't be seen, WHY, and WHAT tool
or access would get it. Never a bare "needs crawl/GSC".

This report is the BASELINE. The generation stage improves against it; the
change report diffs the new content against this snapshot.
