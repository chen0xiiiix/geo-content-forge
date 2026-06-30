# Roadmap

This skill is intentionally scoped: it does ONE thing well now, and grows in
public. The end goal is a beginner-friendly tool where you paste a URL and get a
fully optimized page back. We get there in stages, not in one leap.

## Now, v1.x: single-page SEO + GEO content (this release)

Scope: one page at a time, for users running Claude Code (or any SKILL.md agent).
- Audit the live page (title/meta/H1-H6, keyword classification, issues)
- Real keyword/question demand (free Tier 1; BYOK for volume/difficulty)
- Generate optimized content (constraint-gated, human-voice-gated, GEO-shaped)
- Change report (what changed, why, honest expected effect)
- Evidence labeling throughout (Measured / User-provided / Estimated)

Note on positioning: this is NOT "GEO only". It's SEO (structure, headings,
keyword coverage, technical flags) WITH a GEO layer (citability, answer-first,
schema, recency). GEO sits on top of solid SEO; both ship together.

## Next, v2.x: site-aware

The jump from single-page to site-aware. Requires real crawler code (not just
methodology), so this is a genuine engineering step.
- Full-site crawl (discover + fetch pages, respect robots.txt, rate-limit)
- Internal-link graph: see how pages link, find orphan pages, fix link flow
- Keyword cannibalization: detect pages competing for the same term
- Site-wide content-gap map across all pages
- Optional GSC connection (BYOK) for real indexation/impressions/clicks

## Later, v3.x: beginner SaaS

The end vision: a non-technical user pastes a URL and gets a complete, optimized
page back, covering what to add, rewrite, and update, with zero command line.
- Web interface (paste URL, get results), no Claude Code needed
- One-click "produce the full optimized page structure + content"
- Bilingual (zh/en) mode for brands going global, incl. Chinese AI engines
  (DeepSeek/Kimi/Doubao/Qwen visibility), a near-empty niche today
- This is where it becomes a real SaaS product, not just a skill

## Principle

Ship the focused thing first, grow in public. Each stage is usable on its own.
The build process itself is the story.


---

## Positioning: SEO + GEO, not "GEO only"

This tool is SEO at its core (structure, headings, keyword coverage, internal
links, technical health) WITH a GEO layer on top (citability, answer-first,
schema, recency, AI-citation moves). GEO can't stand alone: AI engines often
cite from pages that already rank, so GEO without solid SEO is a house with no
foundation. Market-facing line: "not just rank on Google, get cited by AI."
Lead with the big SEO need; use GEO as the differentiator.

## v2 module: supporting / long-tail content (topic clusters)

Real need: a core page (e.g. car rental) is strengthened by surrounding long-tail
content (routes, local guides, what's nearby). This builds topic authority and
captures long-tail demand.

THE HARD RULE (this is the easiest place in the whole tool to fabricate):
- Local facts (restaurants, drive times, routes, opening hours) are NOT on the
  user's page and must NEVER be invented by the model.
- Source them from REAL data: maps/places data (BYOK Google Places/Maps), real
  reviews, official tourism/info sources, each fact labeled Measured(source).
- If a fact can't be sourced, mark it "needs local knowledge / API", never write
  a plausible-sounding guess. A fake restaurant or wrong drive time is a
  trust-killing factual error, far worse than a stylistic slip.

Generality: abstract to "core business + the user's surrounding real-world needs
in this context" (travel -> routes/food; dental -> prep/parking; legal -> primer/
local court info). Each industry fills its own surrounding-need types. Geo facts
get a dedicated maps-API tier (BYOK).

## v3 module: multilingual architecture (global coverage)

Real need: cover many markets/languages, not just zh/en.

THE HARD RULE: multilingual is NOT translation.
- Machine-translated pages are detectable, get down-weighted, and read as
  translationese, which directly contradicts the human-voice gate.
- Each language is an INDEPENDENT full run: its own keyword/question demand (how
  that market actually searches), its own local facts, native-level writing (not
  translated), and its own human-voice gate (AI tells differ per language).
- Shared across languages: the constraint framework, GEO standards, evidence
  labeling.
- Generality: don't hardcode "6 languages". The user names whichever languages;
  any language can be added.
- HONESTY: true native-level quality needs a native speaker's final check. The
  tool produces high-quality, data-grounded, structurally-correct multilingual
  content, far better than machine translation, but labels it "native review
  recommended". This is the same honesty as not faking search volume.
- This is a core differentiator for the SaaS, esp. Chinese AI engines
  (DeepSeek/Kimi/Doubao/Qwen), a near-empty niche.

## The beginner-SaaS path (how we get from skill to product)

- START (now): single-page skill, for Claude Code users. Pure methodology, no code.
- JUMP 1 -> site-aware (v2): real crawler code (discover/fetch/parse, link graph,
  cannibalization). This is where it becomes real software, not just SKILL.md.
- JUMP 2 -> full-page autogeneration (v2.5): output a complete, ready-to-ship
  optimized page (add/rewrite/update), stable enough that no hand-editing is
  needed. Hardest quality bar; the no-fabrication defenses matter most here.
- JUMP 3 -> zero-barrier UI (v3, the SaaS): a web page where a non-technical user
  pastes a URL and gets results. Front end, accounts, usage/billing, key
  management, abuse prevention. This is the leap from tool to business.
- Each jump is independently shippable and is itself content. Build in public.

## Business model (honest freemium, not anxiety-bait)

Many SEO audit tools deliberately give a VAGUE free report ("23 issues found!")
that reveals pain but withholds the fix, to manufacture anxiety and force a
subscription. That works, but it conflicts with an honesty-first brand.

This product flips it:
- FREE: a genuinely complete, useful diagnosis (full audit, basic content gen) , 
  nothing hidden to create FOMO. Users feel the quality and honesty up front.
- PAID: things that are genuinely heavier/more valuable, full-site crawl (real
  compute cost), auto-generated complete pages (saves real hours), continuous
  monitoring, multilingual, BYOK data integration, batch processing.
- The difference: bad funnels lock up basic value to force payment; this gives
  basic value generously and charges for genuinely heavier capability.
- Trust converts slower than anxiety but is worth far more for a long-term
  personal brand. Win trust first, then sell the heavy lifting.


## v2 module: off-site content (and the link-spam red line)

Real need: after the on-page content is solid, support it with off-site content
on platforms users and AI trust (Reddit, Quora, YouTube descriptions, industry
directories, Medium, etc.).

CRITICAL DISTINCTION, two different things people wrongly merge:
- OFF-SITE CONTENT (good): genuinely useful content published where it helps real
  readers and where AI engines look. Purpose = real, credible presence.
- LINK BUILDING AT SCALE (forbidden): mass-generating content purely to
  manufacture backlinks. Google calls this link spam. It gets pages down-ranked
  or de-indexed, and it directly betrays the honesty-first brand.

THE RED LINE (design the tool to refuse this, like it refuses to fabricate facts):
- Backlinks are EARNED, not generated. The tool produces content good enough to
  be worth linking to; it never "produces links".
- Off-site content's real GEO purpose is NOT to farm links, it's to make AI see
  true, high-quality information about the business in sources it trusts.
- Every off-site piece must pass the same test as on-site: is this genuinely
  useful to a real reader? It runs the constraint gate and human-voice gate.
- The tool must NOT become a bulk-spam machine (PBNs, low-quality directories,
  mass注水 content). This is a hard product boundary, not a feature toggle.

Correct order: solid on-page (v1) -> real, non-manipulative content on trusted
off-site platforms -> authority and links follow naturally (earned), over time.

Honest limit: even doing off-site content right, the tool only PRODUCES the
content. It can't "win" the link or the trust, that depends on real quality and
time. The tool covers the content-and-structure ~30-40% of SEO; domain authority
and earned links are a longer, mostly off-tool game. Say this plainly; never sell
the tool as an authority/backlink generator.
