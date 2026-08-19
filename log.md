# Wiki Action Log

## [2026-08-18] create | Articles from Razgovor o Islamu (Dervis Hilmi)

Two English wiki articles written from the OCR'd Bosnian book:

- pillar-1/the-prophet-muhammad-his-human-character.md — The Prophet's fully human nature, his trustworthiness (al-Amin), his orphan childhood, the four pillars of his message (Tawhid, equality, justice, freedom), and his character as described in the Quran
- pillar-1/islamic-equality-beyond-lineage.md — Radical Islamic equality: no tribal/lineage privilege, justice enforced even on the Prophet's daughter Fatimah, Bilal and Selman as living proof, condemnation of asabiyyah (tribal loyalty), connection to modern colonialism and racism

Articles follow "Carpati style": every claim cites the source text with page numbers; articles are cross-referenced; written in clear English, not translated word-for-word from Bosnian.

## [2026-08-15] create | Wiki initialized
- Domain: Islamic Foundations + AI Mastery for Halal Success (Sadaqah Jariyah)
- Structure created with SCHEMA.md, index.md, log.md

## [2026-08-15] ingest | TMI Source Material (4 PDFs)
- Source: iCloudDrive/Akhirah/ — July 11, 2026
- Files created:
  - raw/articles/tmi-mission-pledge-edib-2026.md
  - raw/articles/tmi-compass-iirs-edib-2026.md
  - raw/articles/tmi-mirror-portfolio-edib-2026.md
  - raw/articles/tmi-investor-profile-edib-2026.md
- Entity pages: entities/edib-isic.md, entities/tmi-the-muslim-investor.md
- Concept pages: concepts/sadaqah-jariyah.md, concepts/amanah.md, concepts/riba.md, concepts/aaoifi-screening.md
- Comparison page: comparisons/steady-steward-vs-actual-portfolio.md

## [2026-08-15] create | Pillar Pages + Infrastructure
- Created ../pillar-1/
- Created ../pillar-2/
- Created ../pillar-3/
- Created queries/income-model-for-wiki.md
- Created README.md (GitHub-facing)
- Created _config.yml (GitHub Pages)
- Pushed to: https://github.com/edib-isic/islamic-ai-wiki

## [2026-08-15] create | Cornerstone Faith Chapters
- pillar-1/the-quran-your-instruction-manual.md — Quran as instruction manual for humanity: purpose, modern crisis, peace, practical life guidance
- pillar-1/knowing-allah-through-his-names.md — Deep dive into the 99 names, how each transforms your relationship with Allah, work, wealth, and peace (20k+ words)
- pillar-1/work-as-worship.md — How every honest effort becomes ibadah when you understand the right intention
- pillar-1/wealth-in-the-quran.md — Verses about money, trade, charity, and how to handle wealth correctly
- pillar-1/tawakkul-vs-planning.md — Trusting Allah while taking action — what real Tawakkul means
- pillar-1/islamic-business-ethics.md — Principles for halal business success: honesty, fairness, quality, and integrity
- Updated index.md, ../pillar-1/, cross-links between chapters

## [2026-08-15] create | AI for Halal Income Content
- pillar-2/ai-freelancing-roadmap.md — 30-day path to first client
- pillar-2/ai-agency-blueprint.md — Build a halal AI business
- pillar-2/ai-pricing-guide.md — Exact prices for every AI service type
- pillar-2/ai-portfolio-projects.md — 5 projects to build proof
- pillar-2/ai-tools-directory.md — Halal-friendly AI tools
- Updated index.md and ../pillar-2/ with links
- Fixed: converted all wikilinks to standard markdown links

## [2026-08-15] create | Cornerstone Faith Chapter
- pillar-1/the-quran-your-instruction-manual.md — Quran as instruction manual for humanity: purpose, modern crisis, peace, practical life guidance
- pillar-1/knowing-allah-through-his-names.md — Deep dive into the 99 names, how each transforms your relationship with Allah, work, wealth, and peace (20k+ words)
- Updated index.md, ../pillar-1/, cross-links between chapters

## [2026-08-18] update | Added Digitized Books System (Sadqa Jariya)
- Added raw/books/ directory for scanned historical Islamic books
- Added scripts/ocr_book.py — OCR scanned PDFs using Tesseract (supports Arabic, German, Bosnian, English)
- Added scripts/query_books.py — Search extracted text and build LLM-ready context with citations
- Updated SCHEMA.md with book ingestion workflow and citation rules
- Updated index.md with Digitized Books section
- Updated README.md with digitized books explanation

## [2026-08-18] ingest | Razgovor o Islamu by Dervis Hilmi
- First digitized book added to the Islamic AI Wiki.
- Book: Razgovor o Islamu (Conversation About Islam), Dervis Hilmi, Sarajevo 1982, Bosnian.
- Scan: raw/books/razgovor-o-islamu/razgovor-o-islamu-1982.pdf (45 pages)
- OCR: Tesseract 5.5.3 with Bosnian language (bos), 300 DPI.
- Extracted text: raw/books/razgovor-o-islamu/razgovor-o-islamu-extracted.txt (~67k chars)
- Created metadata page: entities/razgovor-o-islam-u.md
- Created author page: entities/dervis-hilmi.md
- Book is now searchable and LLM-queriable with page citations.
