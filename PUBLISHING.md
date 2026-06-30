# Publishing checklist

Before pushing to GitHub, do these:

1. Username (DONE)
   The GitHub username is set to chen0xiiiix in SKILL.md (frontmatter homepage)
   and README.md (clone/install commands). If you ever change it, update both.

2. Confirm the repo name
   Default is `geo-content-forge`. If you rename it, update the same two files.

3. First local run (the real validation)
   This skill has only been exercised in a constrained environment that couldn't
   always fetch raw HTML (403). Run it once in YOUR Claude Code, where it can
   execute scripts/extract_structure.py and use your own Ahrefs data, to confirm
   the 3-tier extraction, fusion, and output behave as designed on a real page.

4. Optional: add a real sample output
   Drop one real end-to-end run into examples/ so visitors see what it produces.

## What's in the repo
- SKILL.md , orchestrator: STEP 0 baseline, core flow, grounding principle,
  constraint framework, GEO standards, human-voice gate, locked output format,
  appended rules (frozen-content + em-dash + minimal-intervention)
- modules/page-type.md , detect page type, apply the right standard
- modules/structure-extraction.md , 3-tier (script / BYOK Ahrefs / fallback)
- modules/audit-report.md , full overview table, single prioritized table
- modules/keyword-intelligence.md , free Tier 1 + BYOK tiers, named competitors
- modules/content-fusion.md , refresh-not-rewrite, voice matching
- modules/change-report.md , diff aligned to the audit baseline
- scripts/extract_structure.py , real HTML parser for full h1-h6
- schema/faqpage.json , JSON-LD template
- examples/sample-brief.md , constraint brief format demo
- ROADMAP.md , v2/v3 vision (site crawl, off-site, multilingual, SaaS, freemium)
- LICENSE , MIT
