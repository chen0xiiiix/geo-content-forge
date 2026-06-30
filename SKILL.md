---
name: geo-content-forge
version: 1.0.0
license: MIT
homepage: https://github.com/chen0xiiiix/geo-content-forge
compatibility: Claude Code, Codex CLI, Cursor, Windsurf, Gemini CLI, and other SKILL.md-compatible agents
description: >
  Writes publish-ready, GEO-optimized on-page content (Title, Meta, H1,
  question-led H2 structure, FAQ with FAQPage JSON-LD) for a real business page.
  Built for AI search (ChatGPT, Claude, Perplexity, Google AI Overviews):
  produces self-contained, citable copy. Unlike audit tools that only score,
  this WRITES the finished content. It works from REAL fetched data (the live
  page, real search questions, real competitor coverage), never from industry
  assumptions; enforces a per-project constraint set; runs a human-voice gate so
  output never reads as AI-written; and labels every claim by evidence level so
  it never passes a guess off as a fact.
when_to_use: >
  Use when the user wants on-page SEO/GEO content WRITTEN or rewritten for a real
  business page under real constraints, including auditing the current page,
  finding real keyword/question opportunities, generating the copy, and reporting
  what changed. Not for keyword research alone or generic site scoring.
triggers: >
  write SEO content, rewrite my page, optimize this page for AI search, GEO
  content, generate title meta H1 FAQ, fix my landing page copy, make my page
  citable, audit and rewrite this page;
  写SEO内容, 改写页面, 优化这个页面, GEO内容, 生成标题描述H1, FAQ内容, 让页面被AI引用,
  内容生产, 落地页文案;
  SEOコンテンツ作成, ページ書き換え, GEOコンテンツ;
  contenido SEO, reescribir página, contenido GEO
---

# STEP 0 , ESTABLISH THE BASELINE (always first, before any analysis)

Before anything else, extract the page's full text and present it RAW. This is
the baseline everything else is built on. This step does ONE thing only:

- Output the COMPLETE visible body text of the page, verbatim, in its ORIGINAL
  language (exclude only the nav menu and footer).
- Do NOT summarize. Do NOT translate (if the page is English, output English; if
  Chinese, output Chinese). Do NOT paraphrase, reorder, or "improve" it.
- Do NOT analyze, judge, or optimize at this step. No findings, no opinions.
- Preserve the original headings/labels and the order they appear in.
- If the full text can't be obtained (e.g. 403 / partial fetch), say so and apply
  the A/B/C fallback in the Grounding Principle , but still output whatever real
  text you do have, verbatim.

The point: a clean, accurate, untouched record of what the page actually says.
Only after the user has this baseline (or it's confirmed) do you move to the
core flow below. Mixing extraction with analysis/translation corrupts the
baseline , keep Step 0 pure.

# THE CORE FLOW (after the baseline , do these 5 steps in order)

1. EXTRACT is done in Step 0 (the verbatim baseline above).
2. IDENTIFY the page type from that text (about/trust, location/landing, product,
   category, homepage, blog, contact). See modules/page-type.md.
3. JUDGE the page against the standard for THAT type, using only the real text.
   (An about page judged as a trust page, a location page as a transactional one.)
4. UNDERSTAND the page's existing tone and voice before changing anything.
5. REWRITE only what needs fixing, in the page's own voice, grounded in the real
   text. Keep the good, fix the specific problems, never a generic clash.

Everything below (the detailed parts and modules) serves this flow. If any detail
seems to complicate it, the flow wins , keep it simple. Step 0 always comes first.

# THE GROUNDING PRINCIPLE (the skill's highest law , overrides everything below)

Every audit finding, every keyword, every generated word, and every change MUST
be grounded in the ACTUAL FULL content of the page as crawled. No exceptions.
This is the standard the whole skill is measured against.

## The mandatory order of work
1. CRAWL THE FULL PAGE FIRST. Get the complete content (and raw HTML for
   structure). Read ALL of it before judging anything.
2. JUDGE ONLY FROM ACTUAL DATA. Every finding traces to something really present
   in the crawled content. Never assert from memory, assumption, or "what this
   kind of page usually has".
3. UNDERSTAND THE WHOLE before touching a part. Before generating any change,
   read the full text, grasp its tone, register, voice, and structure.
4. CHANGE ONLY WHAT NEEDS CHANGING, in the page's own voice. Fixes target the
   specific identified problems and are written to match the page's existing
   tone and style , never a generic rewrite that clashes with the rest.
5. EVERY CHANGE MUST BE SEO-SOUND. Each modification follows professional SEO/GEO
   practice (and the page-type's standard), not guesswork.

## Measured vs Estimated vs N/A (enforced, not optional)
Label everything honestly:
- MEASURED: actually read from the crawled page (quote-able). Counts (word count,
  repetition count) are MEASURED only if you actually counted them in the real
  text , otherwise they are ESTIMATED and must say so.
- ESTIMATED: inferred, approximate, or from competitor/market signals.
- N/A: needs a tool/access you don't have (exact volume, difficulty, full crawl).
Never present an estimate as a measured fact. Never give a number you didn't
actually derive from the real content.

## If you do NOT have the full page (degrade, don't stall)
If the crawler is blocked (e.g. 403) or only partial/rendered text is available,
you do NOT have the full page. Follow this fallback ladder , prefer A/B, and if
neither is provided, proceed with C rather than refusing:

PREFERRED , A or B (authoritative result):
- A: ask the user for an Ahrefs / Screaming Frog / Sitebulb export (full H1-H6
  tree, meta, alt, etc.).
- B: ask the user to paste the raw HTML source (View Source). Parse it with the
  script logic for true full-text + true heading levels.
- With A or B, structure judgments become MEASURED and the audit is authoritative.

FALLBACK , C (proceed anyway, clearly labeled):
- If the user does NOT provide A or B, DO NOT stall or refuse. Produce the result
  using the rendered text you DO have, but:
  - State up front: "Run in fallback mode , raw HTML unavailable (e.g. 403).
    Content judgments are from rendered text; exact heading levels, alt, and
    full-text completeness are NOT verified."
  - Label each item: content read from rendered text = MEASURED (rendered);
    heading levels / alt / anything needing raw HTML = NOT VERIFIED (provide A/B
    to confirm); counts you didn't actually compute = ESTIMATED.
  - Offer the A/B upgrade path at the end, so the user can get the authoritative
    version if they want it.
- The rule: always deliver something useful; never present fallback output as if
  it were fully verified. Usefulness without false confidence.

This principle is the skill's baseline. If any later instruction seems to allow
guessing or skipping the full-content read, THIS principle wins.



# GEO Content Forge

Writes publish-ready, GEO-optimized page content grounded in real data. Audit
tools diagnose; this produces finished copy that is citable by AI search,
compliant with the project's hard rules, evidence-backed, and written in a real
human voice.

Two principles run through everything:
1. NEVER INVENT. Facts come from the fetched page or the user, never from
   "what this industry usually has". If a fact isn't available, say so.
2. LABEL EVIDENCE. Every fact, question, and competitive claim is tagged
   Measured / User-provided / Estimated. A guess is never shown as a fact.

This skill is industry-agnostic: it hard-codes the engine, not any industry's
rules. The caller supplies industry specifics via the Constraint Brief.

---

## Skill Contract (input/output)

- READS: a target URL (or page brief), the primary intent/keyword cluster, the
  project's Constraint Brief (or builds one via intake), an optional voice
  reference, and any optional BYOK keys/exports (DataForSEO/Ahrefs/Semrush, GSC).
- WRITES: a 5-stage deliverable, (1) audit report, (2) keyword intelligence,
  (3) generated content + FAQPage JSON-LD, (4) change report, (5) evidence
  appendix.
- GUARANTEES: every fact traceable to a source and labeled (Measured /
  User-provided / Estimated); constraints enforced; human-voice gate passed; no
  invented metrics; no promised rankings.
- DOES NOT: audit-only/score-only, off-site content, fabricate facts or volume,
  predict ranking/traffic numbers.

## When to use
The user wants on-page content WRITTEN (not just audited) for a real
service-type business page, and cares that output (a) gets cited by AI search,
(b) obeys hard business rules, (c) doesn't read as AI-generated, (d) is based on
the real page and real demand, not assumptions.

Do NOT use for: keyword research alone, backlink analysis, generic site scoring,
or off-site/social content (later versions / separate skills).

---

## Inputs
1. Target URL (preferred) or a detailed page brief
2. Primary intent / keyword cluster
3. Constraint Brief (5 categories, Part 1). Required. If absent, build it via intake.
4. Voice reference (existing copy to match), if available
5. Optional: paid-tool data (DataForSEO/Ahrefs/Semrush exports, GSC). If present,
   use it and label it Measured. If absent, proceed with free sources and label
   accordingly. Never block on paid data.

---

## PART 0 - REAL DATA COLLECTION (hard prerequisite, runs BEFORE writing)

Do not draft a single line until these are done. If a step can't be completed,
record what's missing and label downstream output accordingly. Never fill a gap
with an assumption.

### 0.0 Detect the PAGE TYPE first (modules/page-type.md)
Before auditing, identify the page type (landing/location/service, product,
category/PLP, homepage, about/trust, blog, contact/utility). The type decides the
right standard for every later stage , applying one playbook to all pages is
wrong. An About page missing an FAQ is NOT a flaw; forcing FAQs and keyword
optimization onto a trust page is mis-optimization. If the type is unclear, state
your inference and ask the user to confirm. Carry the type through all 5 stages.

### 0.1 Fetch the actual page + extract structure + run the audit report
Fetch the target URL. Extract structure via modules/structure-extraction.md
(Tier 1 real HTML parser scripts/extract_structure.py -> Tier 2 user's Ahrefs/
export/pasted HTML -> Tier 3 lossy fallback). This is how ALL h1-h6 (incl. H4-H6)
are captured accurately; if a site blocks the parser (403) or the tier is lossy,
SAY SO and ask for an Ahrefs export or HTML, never guess heading levels. Then run
the Page Audit
Report module (modules/audit-report.md) to produce a professional baseline:
title/meta/URL/canonical, full H1-H6 heading tree (flagging missing/duplicate
H1, skipped levels, empty headings), existing schema, word count, image-alt and
link counts, keyword classification (head/long-tail/question/semantic; covered
vs missing), and a prioritized issues list (High/Medium/Low).
- This is how you know what the business actually has. You do NOT know a car
  rental has minibuses (or vans, or a counter) until the page/site says so.
- If the URL can't be fetched: STOP and ask for the page content or a factual
  brief. Do not proceed on industry guesses.
- Everything in the audit is Measured (read from the page). Anything not
  determinable from the page alone (sitewide cannibalization, indexation) is
  marked "needs crawl/GSC", never guessed.
- This audit snapshot is the BASELINE the change report later diffs against.

### 0.2 Collect real demand + keyword opportunities
Run the Keyword Intelligence module (modules/keyword-intelligence.md). It is
tiered and honest:
- TIER 1 (free, default): autocomplete, PAA/related, competitor on-page language,
  forum phrasing. Produces a QUALITATIVE opportunity list (head / long-tail /
  questions / semantic), each backed by evidence, all labeled Measured(source).
- TIER 2 (optional, if a DataForSEO-type key is set): attach real volume /
  difficulty / CPC, labeled Measured(API).
- TIER 3 (optional, if Ahrefs/Semrush key or export provided): merge full data.
HARD RULE: never invent search volume or difficulty. No key = numbers are N/A,
qualitative signal only. State which tier ran. The skill stores no keys and pays
for no data (BYOK: it uses the user's own key/account only if present).

### 0.3 Check competitor coverage (find the gap)
Look at the pages currently ranking / cited for this intent:
- What questions do they already answer, and how deeply?
- Where are they thin, generic, or missing an angle?
- The opportunity is: real demand that competitors cover poorly.
- Tag competitive claims: Measured (observed on their page) or Estimated.

### 0.4 Decide what to write (evidence-gated)
Select the H2s/FAQ topics from the intersection:
  real demand (0.2)  -  what this page already covers (0.1)  -  where competitors
  are weak (0.3).
RULE (from content-gap best practice): every chosen question must carry its
evidence, who searches it (demand source) and why it's an opening (competitor
gap). Never include a question just because it "seems reasonable". If a question
has no demand evidence and no gap evidence, drop it or mark it Estimated and flag
it for user review.

### Honesty boundary (state plainly, don't fake)
This skill does NOT do, and will not pretend to do:
- Exact search volume or keyword difficulty (needs a paid API; mark N/A or ask
  user to supply)
- Any guarantee that content will be cited or indexed (nobody can promise this)
- Real-time "how many times AI mentioned brand X" counts (not reliably available)
When these come up, say so and, if useful, point the user to the proper tool.

---

## PART 1 - CONSTRAINT FRAMEWORK (industry-agnostic)

Every business has hard rules; they fall into 5 universal categories. The caller
fills these per project. The skill presets NOTHING industry-specific.

Constraint Brief template:
  PROJECT: [business / page]
  1. DO-NOT-MENTION   (topics/claims/words that must never appear)
  2. FACT-CORRECTIONS (things commonly gotten wrong that must be stated right)
  3. COMPLIANCE-REDLINES (legal/regulatory limits; claims/guarantees/age, etc.)
  4. VOICE            (the specific tone/register this page must hold)
  5. TERMINOLOGY      (terms to use correctly / words to prefer or avoid)

examples/sample-brief.md shows ONE filled-in brief as a format demo. It is not a
template, not a default, not industry rules.

NO DEFAULTS, EVER:
- Never copy an example's constraints into a real project.
- Two businesses in the same industry can have OPPOSITE constraints (one forbids
  "van" and has no counter; another rents vans and promotes its counter). Follow
  THIS project's brief, never an industry assumption. This mirrors Part 0: facts
  and rules are project-specific, never genre-specific.
- If no brief is supplied, run intake below. Don't guess, don't borrow.
- An empty category is valid (it means "no rules here", not "use the example").

Intake (when the user has no brief): ask plainly , 
- Anything about this business you must NOT say or mention?
- Any facts people commonly get wrong that we must state correctly?
- Any legal/compliance lines we can't cross (claims, guarantees, age limits)?
- How should this page sound? Formal, casual, first-person "we"?
- Any words you must use, or must avoid? Industry terms to get right?
Capture into the 5 categories, confirm, then proceed.

Enforcement (hard-coded, universal): treat every line in the active brief as a
hard gate. Any output violating any line is rejected and rewritten before the
user sees it. Constraints are never softened. If a constraint needs a fact you
don't have, flag the gap (never fabricate).

---

## PART 2 - GEO PRODUCTION STANDARDS (industry-agnostic, hard-coded)

### The unit is the PASSAGE, not the page
AI search uses retrieval-augmented generation: content is chunked, embedded, and
pulled passage-by-passage by semantic relevance. So each passage must stand on
its own. Clarity and self-contained claims beat keyword density.

### Citability shaping
AI search preferentially cites passages that are:
- Self-contained (make sense lifted out of the page, no "as above")
- Answer-first: open with a 40-80 word direct answer to the implied question,
  then expand (AI Overviews cite from the first ~30% of content most often)
- Fact-dense: specific numbers/names/conditions from Part 0, not vague claims
- Right-sized (~130-170 words per citable block)

### High-leverage moves (Princeton GEO research: +30-40% citation visibility)
Apply where truthful and relevant, combined they beat any single move:
- CITE SOURCES: reference authoritative sources where a claim needs backing.
- ADD STATISTICS: concrete figures/percentages (only real ones, from Part 0 or
  cited sources, never invented).
- ADD EXPERT/QUOTED material: a sourced quote where it genuinely adds credibility.
Note: only use these when the facts exist. Never fabricate a stat or quote to
hit the pattern, that breaks the no-fabrication rule.

### Keyword sourcing must be labeled (page vs market)
Every keyword/question used MUST be tagged by where it came from:
- PAGE: terms the existing page already targets (from the audit)
- MARKET: real demand from autocomplete/PAA/search (NZ market reality)
- COMPETITOR: terms named competitors actually cover
This tells the user whether a keyword is "what this page says" vs "what the
market actually searches" , they are different and both matter.

### Question-led architecture
- H2s are the REAL questions from Part 0.2, written in sentence case
- Open each section by answering its question, then support it
- FAQ covers ALL the evidence-gated questions from Part 0.4, the count is
  driven by real demand, NOT a fixed number. If 11 questions have demand + gap
  evidence, write 11. Never cap at an arbitrary number; never pad with invented
  questions either. Quantity = how many real, evidence-backed questions exist.

### Entity clarity
- One primary entity per page + a few supporting entities, consistent naming
  (per Part 0.1 facts)

### Structured data (stacked, not just one type)
- Emit the relevant JSON-LD types together where they fit: FAQPage for the FAQ,
  plus Organization/LocalBusiness and Article where applicable. schema/faqpage.json
  is the FAQ template; add others when the page warrants.
- Schema amplifies meaning, it doesn't create it, the underlying content must
  carry the value. Don't mark up thin content.

### Freshness (AI has a strong recency bias)
- AI citations to a page drop sharply once content is ~3 months old. Where the
  page supports it, include/refresh a "last updated" signal and keep facts current.
- Flag to the user: stale facts (old prices, outdated details) should be updated;
  recency directly affects citation likelihood.

---

## PART 3 - HUMAN-VOICE GATE (mandatory before output)

The biggest lesson from the field: a banned-word list is necessary but NOT
sufficient. What actually removes AI tells is a PROCESS plus structural rules.
Run the process; use the lists as checks within it. Judge by CLUSTERS, not single
words: one stray phrase is fine, two or three together is what reads as AI.

### The process (run these passes, in order)
1. DRAFT freely using only Part 0 facts.
2. CUT FILLER: read each sentence; if a word can go without changing meaning,
   cut it. Aim ~15% shorter.
3. BREAK SYMMETRY: find every parallel scaffold (anaphora, back-to-back
   tricolons, every-bullet-same-shape, two-beat aphoristic closers) and break at
   least one. A passage with zero asymmetry reads as AI.
4. ADD ONE ROUGH EDGE: include at least one genuinely human move, a concrete
   specific, a caveat, a short sentence after a long one, an honest "depends".
   (Within the brand's voice; don't force jokes or slang.)
5. READ ALOUD (mentally): if a real person wouldn't say it to a customer that
   way, rewrite it.

### Layer A - Universal AI tells (check list)
PATTERNS (matter most):
- Negative parallelism (the #1 tell): "It's not just X, it's Y", "Not because X
  but Y", "No X. No Y. Just Z", "The question isn't X, it's Y", and the em-dash
  variant "X - not Y". Kill every variant.
- Metronome rhythm: uniform sentence/paragraph length. Vary it.
- Copulative avoidance: "serves as / stands as / boasts / represents" instead of
  "is / has". Use is/has when true.
- Rule-of-three pile-ups: one tricolon is fine; stacked tricolons are a tell.
- Self-posed rhetorical questions answered in the next breath.
- Sentence-final "-ing" significance tacking: "highlighting its importance",
  "reflecting broader trends", "contributing to...".
- Hollow significance adverbs: "quietly", "deeply", "fundamentally",
  "remarkably", "arguably".
- "just" as a softener; "actually" as fake nuance; hedges ("might/could/perhaps")
  that weaken a claim you actually believe.
- False exclusivity: "what most people miss", "nobody talks about this" used as
  generic filler.
- Entity re-naming every mention; tricolon padding with no specifics.
WORDS/OPENERS: "In today's fast-paced world", "When it comes to", "it's worth
noting", "In conclusion", "Ultimately"; buzzwords: delve, realm, harness, unlock,
tapestry, paradigm, landscape, ecosystem, synergy, cutting-edge, leverage,
robust, empower, streamline, elevate, scalable, holistic, revolutionize,
transformative, seamless, utilize.
FORMAT: sentence case headings, not Title Case. Em dashes: target zero, hard max
one per 1,000 words; replace with commas/periods/parentheses.

### Layer B - Operator's real edits (hands-on signals)
Reject and rewrite on sight: em dashes (remove, restructure); "that said" and
throat-clearing transitions; parallel/balanced clause stacking (排比句); stiff
connectors ("not only... but also..."); empty buzzwords 赋能/一站式/无缝衔接 and
their English equivalents. Goal: how a real person actually talks to a customer.

### Iterate to converge
Run audit -> rewrite up to 2 passes (one rewrite + one corrective pass clears
almost everything; a 3rd rarely finds more). Report passes used.

### IMPORTANT - false-positive disclaimer (especially for non-native English)
This gate is a SIGNAL, not a verdict. The same shapes appear in writing by
non-native English speakers, people under deadline, and technical genres.
Independent audits found AI detectors falsely flag non-native writers at high
rates. So: do NOT mutilate correct, clear copy just to dodge a pattern. This
matters doubly for bilingual/global use, a non-native phrasing is not an "AI
tell" to be scrubbed. Pair the signal with judgment.

### Anti-overcorrection
Don't force slang/jokes, don't make every sentence punchy or every paragraph one
line, don't avoid the single most precise word. Natural is the target, not
"anti-AI" for its own sake. Over-corrected copy reads as fake as AI copy.

## Procedure
1. PART 0 first: DETECT PAGE TYPE (0.0, modules/page-type.md) to set the right
   standard, then fetch page + run AUDIT REPORT (0.1, modules/audit-report.md),
   collect demand + run KEYWORD INTELLIGENCE (0.2, modules/keyword-intelligence.md),
   check competitors (0.3), evidence-gate the topic list (0.4). If blocked, ask;
   never assume.
2. Load Constraint Brief (Part 1) or run intake.
3. Draft Title, Meta, H1, question-led H2s, FAQ, using ONLY Part 0 facts and
   applying Part 2 standards as you write.
4. Constraint gate (Part 1): any violation, rewrite.
5. Human-voice gate (Part 3, both layers): any tell, rewrite.
6. Emit FAQPage JSON-LD (schema/faqpage.json).
7. CHANGE REPORT (modules/change-report.md): diff the new content against the
   0.1 audit snapshot, classify each element NEW / REWRITTEN / REMOVED /
   UNCHANGED, give the reason for significant changes, and an HONEST qualitative
   expected-effect note (never a predicted number; suggest GSC tracking).
8. Output in requested format (.docx if asked, else clean markdown), WITH the
   evidence note (Measured / User-provided / Estimated per major item).

## Output format, LOCKED SKELETON (always produce exactly this shape)

Every run MUST be presented in these 5 numbered stages, in order, with the
markers shown. This structure is fixed: staged headers + explicit gate
checkmarks + tables for the diff + an evidence appendix. Do not deviate from the
skeleton; only the contents change per page.

ONE CROSS-CUTTING RULE (applies to all stages):
- NO RE-DESCRIBING: state each fact in FULL once (in the audit), then in later
  stages REFERENCE it, don't repeat the detail. e.g. Stage 4 writes "opening-hours
  conflict (see audit) -> unify", not the full description again. This kills
  redundancy while keeping the audit->change->evidence traceability chain.

### Stage 1 · Audit report
- One-line health verdict (5-second read).
- Prioritized issues list: HIGH / MEDIUM / LOW, each item one line
  "[what] -> [fix]".
- Full detail (collapsible/after the list): snapshot table, full H1-H6 heading
  tree with inline flags, keyword classification table (head/long-tail/question/
  semantic; covered vs missing).
- Scope-boundary notes for anything single-page analysis can't see (explain
  why + what tool/access is needed; never a bare "needs crawl").

### Stage 2 · Keyword intelligence
- Tier banner (which tier ran; volume/difficulty = N/A unless a key tier ran).
- Opportunity clusters: questions / long-tail / semantic, each WITH its evidence
  (which free signal supports it). Labels: Measured / Estimated.

### Stage 3 · Generated content
- Title (with char count)
- Meta description (with char count)
- H1
- Question-led H2/H3 outline (one-line intent each)
- FAQ: ALL evidence-gated Q&A (count driven by real demand, NO fixed cap), each
  answer citability-shaped (answer-first, ~130-170 words, self-contained)
- Stacked JSON-LD , OUTPUT THE ACTUAL CODE, not a mention. Produce complete,
  copy-paste-ready <script type="application/ld+json"> blocks with the page's REAL
  data filled in (FAQPage with the real Q&A; LocalBusiness with real name/address/
  phone/hours; Article where applicable). A developer must be able to paste it
  directly. Never write "add schema" without the actual filled code.
- GATE CHECKS, shown explicitly with ✓ / ✗ per item:
    Constraint gate: list EACH line from the ACTIVE project's Constraint Brief
      and check it ✓ (for a law firm these are the law firm's rules, for a
      restaurant the restaurant's , the gate reflects whatever industry's brief
      is loaded, never hardcoded car-rental rules)
    Human-voice gate: em dash ✓ / negative-parallelism ✓ / metronome ✓ /
      copulative ✓ / buzzwords ✓ / sentence-case headings ✓ (passes used: N)

### Stage 4 · Change report (table-led, bottom-line first)
- LINE 1: one-sentence bottom line (what changed + net effect).
- Diff TABLE: | Element | Before | After | Type (NEW/REWRITTEN/REMOVED/UNCHANGED) |
- "Why it matters": one line each, only for significant changes.
- Expected effect: 2-3 sentences, honest, qualitative, + GSC tracking suggestion.
- Hard bugs found but needing human fix (if any), listed separately.
- Counts: X new, Y rewritten, Z removed, W flagged for your decision.

### Stage 5 · Evidence appendix
- Measured (from page) / Measured (from competitors-SERP) / Estimated /
  User-provided, each listing what falls under it.
- N/A (needs paid tool): e.g. exact volume, difficulty, ranking prediction.
- Needs crawl / GSC: e.g. full cannibalization, indexation status.

## What this skill deliberately does NOT do
No scoring/auditing, no off-site content, no fabricated facts, no faked metrics.
It will not invent business details, will not present estimates as measured, will
not promise indexing/citation, will not drop a constraint to make writing easier.
It covers ONE page type well rather than many poorly (more types = later version).

---

# APPENDED RULES (additive only, never modify the content above)

## How this file is maintained
The content above this line is FROZEN. New rules and refinements are only ever
APPENDED below, never edited into the sections above. Established decisions are
permanent; optimization stacks on top, it does not rewrite what's already agreed.

## Em dash rule (reinforced)
No em dashes or en dashes anywhere, not in the skill, not in any audit, and not
in any generated/rewritten content. This has been stated repeatedly and is
absolute. When listing items, use commas and the word "and" (e.g. "name, phone
number, licence plate, and insurance information"), or split into separate
sentences. Before returning ANY output, scan for the dash characters and remove
every one. A single em dash in delivered output is a rule violation.

## DEFAULT TO NOT TOUCHING (minimal-intervention principle)

The core of GEO is making content machine-readable and citable, primarily via
structured data (schema). It is NOT rewriting the page's content. Default to
leaving the page exactly as it is.

On an existing page that already works, only do:
1. ADD what's genuinely missing for GEO, schema above all (FAQPage, LocalBusiness,
   Organization, etc.). This is additive and changes no visible copy.
2. FIX only true errors: real duplicates, actual grammar mistakes, broken links,
   factual conflicts. A "true error" is something objectively wrong, not a style
   preference.

Do NOT, by default:
- rewrite headings that are already clear (keep "About deposit", don't turn it
  into a question)
- regroup or reorder sections that already have a working logic
- reword answers that are merely stiff or non-native but correct in meaning
- impose a "better" structure of your own

Stiff or slightly non-native phrasing that is NOT wrong is LEFT ALONE by default.
Only touch wording when the user explicitly asks for a language pass, or when it
is an actual error. Preserve the owner's voice, structure, and wording. The win
comes from schema and correctness, not from a rewrite. When in doubt, don't
change it.
