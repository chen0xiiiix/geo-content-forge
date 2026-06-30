#!/usr/bin/env python3
"""
extract_structure.py , reliable on-page SEO structure extraction from RAW HTML.

WHY THIS EXISTS: reading rendered/simplified text loses tag-level information
(e.g. an <h4> can look identical to bold text). Tools like Ahrefs parse the raw
HTML source. This script does the same: it fetches the raw HTML and parses the
actual tags, so the audit sees EVERY h1-h6, canonical, schema, etc. , not an
approximation.

Usage: python extract_structure.py <url>
Outputs JSON to stdout with the full, accurate structural inventory.

Dependencies: requests, beautifulsoup4, lxml
  pip install requests beautifulsoup4 lxml --break-system-packages
"""
import sys, json, re

def extract(url):
    import requests
    from bs4 import BeautifulSoup

    headers = {"User-Agent": "Mozilla/5.0 (compatible; geo-content-forge/1.0; SEO audit)"}
    resp = requests.get(url, headers=headers, timeout=20)
    resp.raise_for_status()
    html = resp.text
    soup = BeautifulSoup(html, "lxml")

    def txt(el):
        return re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip()

    # Headings: every h1-h6, IN DOCUMENT ORDER, with level
    headings = []
    for el in soup.find_all(re.compile(r"^h[1-6]$")):
        headings.append({"level": int(el.name[1]), "text": txt(el)})

    # Heading counts
    counts = {f"h{i}": sum(1 for h in headings if h["level"] == i) for i in range(1, 7)}

    # Hierarchy skip detection (e.g. h1 -> h3 with no h2 between)
    skips = []
    prev = 0
    for h in headings:
        if prev and h["level"] > prev + 1:
            skips.append(f"h{prev} -> h{h['level']} (skips h{prev+1})")
        prev = h["level"]

    # Title / meta
    title = txt(soup.title) if soup.title else None
    def meta(name=None, prop=None):
        if name:
            t = soup.find("meta", attrs={"name": name})
        else:
            t = soup.find("meta", attrs={"property": prop})
        return t.get("content", "").strip() if t and t.get("content") else None

    # Canonical
    can = soup.find("link", attrs={"rel": "canonical"})
    canonical = can.get("href") if can else None

    # Schema / JSON-LD types present
    schema_types = []
    for s in soup.find_all("script", attrs={"type": "application/ld+json"}):
        try:
            data = json.loads(s.string or "{}")
            items = data if isinstance(data, list) else [data]
            for it in items:
                t = it.get("@type")
                if t:
                    schema_types.append(t)
        except Exception:
            schema_types.append("UNPARSEABLE_JSON_LD")

    # Images / alt
    imgs = soup.find_all("img")
    missing_alt = [img.get("src", "?") for img in imgs if not img.get("alt", "").strip()]

    # Links
    internal, external = 0, 0
    from urllib.parse import urlparse
    base = urlparse(url).netloc
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:"):
            continue
        netloc = urlparse(href).netloc
        if netloc == "" or netloc == base:
            internal += 1
        else:
            external += 1

    # Word count (visible body text)
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    body_text = soup.get_text(" ", strip=True)
    word_count = len(body_text.split())

    return {
        "url": url,
        "title": title,
        "title_length": len(title) if title else 0,
        "meta_description": meta(name="description"),
        "meta_description_length": len(meta(name="description") or ""),
        "canonical": canonical,
        "og": {
            "title": meta(prop="og:title"),
            "description": meta(prop="og:description"),
            "image": meta(prop="og:image"),
        },
        "headings_in_order": headings,
        "heading_counts": counts,
        "hierarchy_skips": skips,
        "schema_types": schema_types,
        "images_total": len(imgs),
        "images_missing_alt": missing_alt,
        "internal_links": internal,
        "external_links": external,
        "word_count": word_count,
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "usage: python extract_structure.py <url>"}))
        sys.exit(1)
    try:
        print(json.dumps(extract(sys.argv[1]), indent=2, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)
