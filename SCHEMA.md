# Wiki Schema

## Domain
Islamic Foundations + AI Mastery for Halal Success. A sadaqah jariyah knowledge base that bridges knowing Allah, earning halal through AI, and teaching others to benefit — structured so anyone can learn, teach, and act on it forever.

Three pillars:
1. **Faith & Knowing Allah** — Quran, Sunnah, and Islamic principles on work, trade, knowledge, wealth, and ethics
2. **AI for Halal Income** — Practical paths to earn through AI: agencies, freelancing, consulting, tools, services
3. **Teaching Frameworks** — Lesson plans, course outlines, scripts so others can teach others

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `islamic-principles-on-wealth.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use `[wikilinks.md](wikilinks.md)` to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- **Provenance markers:** On pages that synthesize 3+ sources, append `^[raw/articles/source-file.md]` at the end of paragraphs whose claims come from a specific source
- Islamic citations use standard format: `[Surah:Ayah]` for Quran, `[Book# hadith# — grading]` for Hadith

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
---
```

### raw/ Frontmatter
Raw sources get a small frontmatter block so re-ingests can detect drift:
```yaml
---
source_url: https://example.com/article
ingested: YYYY-MM-DD
sha256: <hex digest of the raw content below the frontmatter>
---
```

## Tag Taxonomy

**Faith & Knowledge:**
- faith, quran, sunnah, hadith, aqeedah, ibadah, adab, ethics, halal-haram, dua, tawakkul

**Wealth & Work:**
- work, trade, wealth, rizq, halal-income, entrepreneurship, business-ethics, sadaqah-jariyah

**AI & Tech:**
- ai, ai-tools, ai-agency, ai-freelancing, ai-consulting, ai-products, ai-services, ai-business-model

**Teaching & Impact:**
- teaching, course-design, content-creation, coaching, community-building, knowledge-sharing

**Meta:**
- comparison, timeline, case-study, resource-list, framework, strategy

Rule: every tag on a page must appear in this taxonomy. Add new tags here first before using them.

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details, or things outside the domain
- **Split a page** when it exceeds ~200 lines — break into sub-topics with cross-links
- **Archive a page** when its content is fully superseded — move to `_archive/`, remove from index

## Page Types

### Faith Pages
Islamic knowledge pages include:
- Primary sources cited (Quran verses, authentic hadith)
- Scholar positions where relevant (especially on fiqh matters)
- Clear separation between established rulings and opinion
- Connection to practical AI/business questions where applicable

### AI Business Pages
Income and strategy pages include:
- Concrete, actionable steps (not vague "learn AI" advice)
- Real tools, platforms, and pricing
- Halal/haram considerations flagged where relevant
- Cost estimates, time estimates, and difficulty level
- Updated regularly — AI moves fast

### Teaching Framework Pages
Ready-to-deploy educational material:
- Clear learning outcomes
- Modular structure (can be used as a full course or individual lessons)
- Exercises, examples, and assessment ideas
- Notes on delivery method (video, text, live, etc.)

## Update Policy
When new information conflicts with existing content:
1. Check dates — newer sources generally supersede older ones
2. For Islamic rulings, prioritize authentic primary sources over modern opinion
3. If genuinely contradictory, note both positions with dates/sources
4. Mark contradictions in frontmatter: `contradictions: [page-name]`
5. Flag for user review in lint report
