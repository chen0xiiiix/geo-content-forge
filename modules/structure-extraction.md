# Structure Extraction Module (get EVERY tag, like Ahrefs does)

WHY: reading rendered/simplified text loses tag-level info. An <h4> can look
identical to bold text in rendered output. Professional tools (Ahrefs, Screaming
Frog) parse RAW HTML source, so they catch every h1-h6. This skill must do the
same, and be honest when it can't.

## The three tiers (use the best available; never fake precision)

### Tier 1 , own parser (free, but blockable)
Run scripts/extract_structure.py <url>. It fetches raw HTML and parses actual
tags with BeautifulSoup: every h1-h6 in order, canonical, JSON-LD types, OG tags,
alt coverage, links, word count.
- When it works: fully accurate structure, including ALL H4/H5/H6.
- LIMITATION: many sites return 403/blocked to simple scripts (anti-bot/CDN).
  If blocked, DO NOT fall back to guessing from rendered text and pretend it's
  complete. Go to Tier 2/3 and SAY the structure came from there.

### Tier 2 , user's professional tool (BYOK, reliable)
If the user has Ahrefs / Screaming Frog / Sitebulb / DataForSEO, accept their
export or pasted data. This is the most reliable source (their infra rotates IPs,
renders JS, defeats anti-bot). Label: Measured (user's Ahrefs/etc.).
- If the user pastes raw HTML, parse THAT with the script logic , also reliable.

### Tier 3 , rendered fetch (fallback, lossy)
A browser-style fetch (e.g. web_fetch) usually gets in, but returns rendered text
where heading LEVELS may be ambiguous (h4 vs bold). Use only as last resort, and
explicitly flag: "heading levels approximate , source did not expose raw tags;
provide Ahrefs export or HTML for exact levels."

## Mandatory honesty
State which tier produced the structure data. If H4-H6 levels could not be
verified from raw HTML, say so , never silently omit them or guess. Missing data
is information: report "H4: not verifiable at this tier" rather than nothing.

## Always list H1 through H6 explicitly
In the audit overview, show a row for EACH of H1, H2, H3, H4, H5, H6. If a level
has none, write "none found". Never skip a level in the report just because the
page (or the fetch) didn't surface it , distinguish "page has none" from "not
captured at this tier".
