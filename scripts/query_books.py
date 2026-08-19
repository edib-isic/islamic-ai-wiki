#!/usr/bin/env python3
"""
query_books.py — Search extracted book text and build LLM-ready context.

Usage:
    python scripts/query_books.py "How do I perform wudu?" --top 10
    python scripts/query_books.py "rulings on combining prayers" --top 15 --lang ar

This script:
- Reads all extracted text files under raw/books/
- Searches for relevant passages matching the query
- Returns top N passages with citations (book, page)
- Output is formatted for pasting into an LLM prompt
"""

import argparse
import os
import re
import sys
from pathlib import Path


BOOKS_DIR = Path(__file__).resolve().parent.parent / "raw" / "books"


def find_text_files():
    return sorted(BOOKS_DIR.rglob("*-extracted.txt"))


def extract_passages(text, pages, query, window=4):
    """
    Split text by page markers and return passages near query matches.
    Returns list of (page_num, passage_text, book_name).
    """
    lines = text.split("\n")
    passages = []
    current_page = None
    page_lines = {}

    # Group lines by page
    for line in lines:
        m = re.match(r"^=== PAGE (\d+) ===$", line.strip(), re.IGNORECASE)
        if m:
            current_page = int(m.group(1))
            page_lines[current_page] = []
            continue
        if current_page is not None:
            page_lines[current_page].append(line)

    # Search for query terms
    query_terms = [t.lower() for t in query.split() if len(t) > 2]
    if not query_terms:
        return []

    for page_num, lines in page_lines.items():
        page_text = "\n".join(lines)
        page_lower = page_text.lower()

        # Check if page contains query terms
        matches = sum(1 for t in query_terms if t in page_lower)
        if matches >= 1:
            # Build a passage centered around the first match
            first_term = next((t for t in query_terms if t in page_lower), None)
            if first_term:
                idx = page_lower.index(first_term)
                start = max(0, idx - 200)
                end = min(len(page_text), idx + 400)
                passage = page_text[start:end]
                if start > 0:
                    passage = "..." + passage
                if end < len(page_text):
                    passage = passage + "..."
                passages.append((page_num, passage, matches))

    # Sort by match count (most relevant first)
    passages.sort(key=lambda x: x[2], reverse=True)
    return [(p, txt) for p, txt, _ in passages]


def search_books(query, top_n=10):
    """Search all books and return top N passages with citations."""
    text_files = find_text_files()
    if not text_files:
        print("[INFO] No extracted text files found in raw/books/")
        print("       Scan and OCR your first book to begin.")
        return []

    all_passages = []

    for tf in text_files:
        book_dir = tf.parent
        book_name = book_dir.name
        rel_path = tf.relative_to(BOOKS_DIR.parent.parent)

        try:
            with open(tf, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
        except Exception as e:
            print(f"[WARN] Could not read {tf}: {e}")
            continue

        passages = extract_passages(text, None, query)
        for page_num, passage in passages:
            citation = f"{rel_path}, page {page_num}"
            all_passages.append((citation, book_name, passage))

    # Sort by relevance (we'll use a simple heuristic: position in list from best-matching book)
    # For now, just return top N
    all_passages = all_passages[:top_n]
    return all_passages


def format_context(passages):
    """Format passages as LLM-ready context with citations."""
    if not passages:
        return "[No relevant passages found in the books.]"

    lines = [
        "You are an Islamic scholar assistant. Answer the user's question using ONLY the passages below.",
        "Cite your sources explicitly using [source, page] format.",
        "If the passages do not contain enough information, say so clearly.",
        "",
        "## Source Passages",
    ]

    for i, (citation, book_name, passage) in enumerate(passages, start=1):
        lines.append(f"### [{i}] {book_name}")
        lines.append(f"Source: {citation}")
        lines.append(f"```\n{passage.strip()}\n```")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Search extracted book text")
    parser.add_argument("query", help="Search query")
    parser.add_argument(
        "--top",
        type=int,
        default=10,
        help="Number of top passages to return (default: 10)",
    )
    parser.add_argument(
        "--prompt-only",
        action="store_true",
        help="Output full LLM prompt ready to paste",
    )
    args = parser.parse_args()

    passages = search_books(args.query, top_n=args.top)

    if not passages:
        print("[INFO] No relevant passages found.")
        sys.exit(0)

    if args.prompt_only:
        print("=" * 60)
        print("LLM PROMPT — copy everything below and paste into your LLM:")
        print("=" * 60)
        context = format_context(passages)
        print(context)
        print("=" * 60)
        print(f"USER QUESTION: {args.query}")
        print("=" * 60)
    else:
        print(f"Found {len(passages)} relevant passage(s):\n")
        for i, (citation, book_name, passage) in enumerate(passages, start=1):
            print(f"[{i}] {book_name}")
            print(f"    {citation}")
            preview = passage[:300].replace("\n", " ")
            print(f"    ...{preview}...")
            print()


if __name__ == "__main__":
    main()
