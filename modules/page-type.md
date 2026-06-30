# Page-Type Detection Module (decide the standard BEFORE optimizing)

WHY: page type determines the right optimization strategy. Applying one playbook
to every page is malpractice. An About page is not a landing page; forcing FAQs
and keyword optimization onto a trust page is mis-optimization. Detect type
first (Part 0, before audit), then apply the matching standard.

## Detect the page type (from URL, title, H1, content pattern)

- TRANSACTIONAL LANDING / LOCATION / SERVICE: targets commercial/local search,
  goal = rank + convert + get cited. (e.g. /locations/..., a service page)
- PRODUCT (single SKU): specific product terms, goal = convert; specs + reviews.
- CATEGORY / COLLECTION (PLP): broader commercial terms; short intro copy +
  product list + faceted nav; ItemList/BreadcrumbList schema.
- HOMEPAGE: brand + 1-2 head terms; serves all funnel stages; not over-optimized
  for one keyword.
- ABOUT / TRUST / BRAND: goal = trust, NOT keyword ranking. Optimize credibility
  signals, native-quality writing, technical health. Do NOT bolt on FAQs or
  keyword density. Organization schema fits.
- BLOG / INFORMATIONAL: top-of-funnel; answer-first, depth, internal links to
  commercial pages; Article schema.
- CONTACT / UTILITY: minimal; correct NAP, LocalBusiness schema, technical only.

If unsure, state your best inference + why, and ask the user to confirm before
applying a standard.

## Apply the matching standard

| Page type | Optimize for | DO | DON'T |
|---|---|---|---|
| Landing/Location/Service | rank + convert + cite | Q-led H2s, citable FAQ, LocalBusiness/FAQPage schema, constraints, voice | - |
| Product | convert | unique copy, specs, reviews, Product schema | duplicate descriptions |
| Category/PLP | broad commercial rank | short intro copy, internal links, ItemList/Breadcrumb schema, optional mini-FAQ | thin grid w/ no context |
| Homepage | brand + few head terms | clear value prop, internal links, Organization schema | over-optimize one keyword |
| About/Trust | trust + credibility | native rewrite, trust signals (years, scale, team, reviews), Organization schema, tech health | forcing FAQ / keyword optimization |
| Blog/Info | inform + funnel users | answer-first, depth, internal links, Article schema | hard selling |
| Contact/Utility | correctness | NAP, LocalBusiness schema, tech health | content padding |

## Effect on the 5 stages
- Stage 1 audit: judge against the TYPE's standard (e.g. an About page missing an
  FAQ is NOT a flaw; missing H1 or native-quality copy IS).
- Stage 2 keywords: for About/Contact, keyword/competitor-keyword analysis is
  largely N/A; record trust-signal gaps instead.
- Stage 3 generate: apply the type's DO/DON'T. Match GEO depth to the type.
- Stage 4/5: unchanged structure; reasons reference the type's standard.
