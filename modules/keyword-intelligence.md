# Keyword Intelligence Module (BYOK-tiered)

Purpose: find real keyword/question opportunities for a page WITHOUT pretending
to have data the skill doesn't have. Three tiers, free by default, upgradeable
if the user brings their own API key. Every output is evidence-labeled.

CORE HONESTY RULE: exact search volume and keyword difficulty CANNOT be derived
for free. They require a paid data infrastructure (Google's own data, or vendors
like DataForSEO/Ahrefs/Semrush who scrape and model it at scale). The skill must
NEVER invent these numbers. No key = qualitative signal only, clearly labeled.
Inventing a volume or difficulty score is a fabrication and is forbidden.

---

## TIER 1 - FREE (default, always available, no key)

Collect real demand signals from public sources. Everything here is genuinely
free and reflects real searching behaviour. Label all of it Measured (source).

1. Autocomplete / Suggest
   - Pull Google autocomplete expansions for the seed terms (a-z, "for", "near",
     "how", "best", etc.). Terms that autocomplete = real, frequent searches.
   - Source label: Measured (Google Suggest).

2. People Also Ask + Related Searches
   - Pull PAA questions and "related searches" for the core query.
   - These are real questions/phrasings people use.
   - Source label: Measured (SERP PAA / related).

3. Competitor on-page language (NAME them + list their coverage in DETAIL)
   - Fetch the top competitor pages for the intent. Extract, in detail, the
     actual content each one covers: which keywords/phrasings appear, which
     questions their FAQ answers, what topics/sections they include, and how
     deep each is (thin mention vs full section).
   - Output a DETAILED per-competitor table (content-level, all Measured from
     their live page):
       | Competitor | Keywords/phrases used | Questions answered | Topics/sections covered | Depth | Visible gap |
       |---|---|---|---|---|---|
       | GO Rentals | "airport car hire", "cheap rental" | how to collect, insurance, fuel policy | pickup steps, fleet list, insurance, locations | deep on airport, thin on city | no downtown/CBD angle |
       | Snap Rentals | "budget car rental akl" | age policy, shuttle, what to bring | shuttle, age rules, fleet | medium | no off-hour detail |
   - The point: show specifically WHAT each competitor covers and HOW WELL, so
     the content gap is concrete, not a vague "competitors are thin".
   - Only name REAL competitors actually found; never invent names or coverage.
   - HONESTY BOUNDARY: content-level coverage above = Measured (their page).
     Their exact RANKING keywords / search volume / traffic / difficulty needs a
     paid tool (Ahrefs/Semrush) , mark N/A unless the user supplies that data.
   - Source label: Measured (named competitor page, content-level).

4. Forum / community phrasing (where relevant)
   - Real questions from Reddit/forums for how actual people phrase needs.
   - Source label: Measured (forum) or Estimated if inferred.

WHAT TIER 1 OUTPUTS:
- A QUALITATIVE opportunity list: which terms/questions are clearly real and
  in-demand (they appear in autocomplete / PAA / multiple competitors), grouped
  as: head terms, long-tail variants, question phrasings, semantic/related terms.
- It does NOT output volume or difficulty numbers. For each cluster it states
  the EVIDENCE (e.g. "appears in autocomplete + 3 competitor pages") instead of
  a fake metric.
- Explicitly note: "Precise volume/difficulty not available at this tier; see
  Tier 2/3 to add it."

This tier alone is enough to WRITE good content. Volume numbers refine
prioritization; they are not required to identify real demand.

---

## TIER 2 - BYOK, low cost (optional: DataForSEO or similar pay-per-call API)

If the user has set a DataForSEO (or equivalent) API key in their environment:
- Call the SERP/keyword endpoints to attach REAL search volume, keyword
  difficulty, CPC, and SERP feature data to the Tier 1 clusters.
- This is pay-per-call (cents per query), far cheaper than monthly Ahrefs/Semrush.
- Label everything from the API: Measured (DataForSEO).
- The skill NEVER bills anyone: it uses the user's own key, the user's own
  account, the user's own cost. The skill only calls the endpoint IF a key exists.

If no key is set: skip silently, stay on Tier 1, and note volume/difficulty as
N/A (key not provided). Do not block, do not guess.

---

## TIER 3 - BYOK, full suite (optional: Ahrefs/Semrush key or manual export)

If the user already pays for Ahrefs/Semrush:
- Accept an API key OR a manual CSV export from those tools.
- Merge their richer data (ranking keywords, competitor keyword gaps, backlink
  context) into the opportunity list.
- Label: Measured (Ahrefs/Semrush, user-provided).

If unavailable: skip, stay on whatever lower tier is available.

---

## BYOK mechanics (how "bring your own key" works, plainly)

- The skill stores NO keys and pays for NO data.
- It reads a key from the user's environment (e.g. DATAFORSEO_KEY, AHREFS_KEY)
  ONLY if the user has set one.
- Key present -> richer, numeric, Measured(API) output.
- Key absent -> Tier 1 qualitative output, with numeric fields marked N/A.
- This keeps the open-source skill free for everyone, costs the author nothing,
  and never fabricates metrics. Professionals who want numbers plug in their own
  paid account.

---

## Output contract for the keyword stage

Always return:
- Opportunity clusters (head / long-tail / questions / semantic), each with its
  EVIDENCE (which free signals support it) and, IF a key tier ran, its real
  volume/difficulty labeled Measured(API).
- A clear tier banner: "Ran at Tier 1 (free signals only). Volume & difficulty
  N/A - add a DataForSEO/Ahrefs key to populate." (adjust to whichever tier ran)
- Never a bare number without a source label. Never an invented number.
