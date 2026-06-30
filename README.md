# GEO Content Forge

A Claude Code skill that **writes** publish-ready, GEO-optimized on-page content,
grounded in real data and labeled by evidence. Not another audit tool.

Most SEO tools either diagnose OR generate. This runs the full workflow on a
real page, end to end:

1. **Audit** the live page (title, meta, full H1-H6 tree with flags, keyword
   classification, prioritized issues), the baseline.
2. **Keyword intelligence**, real demand from free signals (autocomplete, PAA,
   competitor language), with optional BYOK upgrade for real volume/difficulty.
3. **Generate** the finished content (Title, Meta, H1, question-led H2s, FAQ +
   FAQPage JSON-LD) using only verified facts.
4. **Change report**, element-by-element diff vs the live page (new / rewritten
   / removed), with reasons and an honest, qualitative expected-effect note.
5. **Evidence appendix**, every fact labeled Measured / User-provided / Estimated.

It never passes a guess off as a fact, never invents search volume, and never
promises a ranking.

## What makes it different

- **Generates, not just scores.** Output is paste-ready copy.
- **Grounded in real data, never assumptions.** It fetches the actual page to
  learn what the business actually has (not what the industry "usually" has),
  pulls real People-Also-Ask demand, and checks competitor coverage before
  writing a word. No fetch, no fabrication: if it can't verify, it asks.
- **Evidence-labeled.** Every fact, question, and competitive claim is tagged
  Measured / User-provided / Estimated. An estimate is never shown as a fact.
- **Constraint-gated.** Hard do-not-mention rules are enforced, not suggested.
  Industry-agnostic: you supply your project's rules; the skill presets nothing.
- **Human-voice gate.** Every output is scanned for AI tells (negative
  parallelism, metronome rhythm, copulative avoidance, buzzwords, em dashes...)
  and rewritten until it passes, with a guard against over-correction.
- **Honest about its limits.** It does not fake search volume, does not promise
  indexing/citation, and flags where a paid tool is needed.

## Why this exists

Running real SEO for real businesses, the bottleneck is rarely "what's wrong."
It's producing copy that gets cited AND obeys the constraints every real business
has, based on what's actually true for that business, in a voice that doesn't
read as machine-written. Audit tools don't do that. This does.

## Install

```bash
git clone https://github.com/chen0xiiiix/geo-content-forge.git
cp -r geo-content-forge ~/.claude/skills/geo-content-forge
```

## Usage

Give it a target URL, the page intent, your Constraint Brief (or let it walk you
through one), and a voice reference if you have one. It collects real data first,
then returns finished copy plus an evidence appendix showing what was measured
versus estimated.

## Quick start

Copy one of these to begin (English or Chinese):

```
Audit and rewrite the SEO content for https://example.com/page,
here are my constraints: [your do-not-mention / facts / voice rules]
```
```
Optimize this page for AI search: https://example.com/page , 
find the real questions people ask and generate citable FAQ content
```
```
帮我审计并改写 https://example.com/page 的 SEO 内容，
我的约束是：[不能提的 / 必须说对的事实 / 语气要求]
```
```
优化这个页面让它更容易被 AI 引用：https://example.com/page
```

If you don't have a constraint brief ready, just give the URL, the skill will
walk you through building one.

## Optional: paid data

If you provide DataForSEO / Ahrefs / Semrush exports or GSC data, it uses them
and labels them Measured. Without them it works from free sources (live fetch,
SERP questions, autocomplete) and labels accordingly. It never blocks on paid
data, and never fakes the metrics it can't get for free.

## What's inside

- `SKILL.md`, the orchestrator (5-stage workflow, constraint framework, GEO
  standards, human-voice gate)
- `modules/audit-report.md`, professional on-page audit (the baseline)
- `modules/keyword-intelligence.md`, 3-tier keyword opportunities (free + BYOK)
- `modules/change-report.md`, honest before/after diff and expected effect
- `examples/sample-brief.md`, one filled-in constraint brief (format demo)
- `schema/faqpage.json`, FAQPage JSON-LD template

## Roadmap (skill chain)

This is stage one: on-page content for a single page type. Planned companions
that chain off this skill's outputs:
- off-site content generation (forum/Q&A/directory copy AI search trusts)
- multi-page-type support (product, comparison, article, hub pages)
- a bilingual (zh/en) mode for brands going global

## License

MIT
