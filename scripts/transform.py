#!/usr/bin/env python3
"""Deterministic transformer: mirror/{docs,reference}/*.md -> preview repo .mdx files.

Applied fixes:
  * Strip ReadMe boilerplate footer/header (llms.txt hint line, updatedAt frontmatter).
  * Extract H1 as title, following lead paragraph as description (if it looks like a lead).
  * Convert ReadMe emoji callouts (`> 📘 ... / > ⚠️ ...`) into Mintlify Info/Note/Warning/Tip/Danger blocks.
  * Convert `<HTMLBlock>{` ... `}</HTMLBlock>` iframe wrappers to a plain <iframe/> in a <Frame>.
  * Convert `[block:image]{json}[/block]` widgets to a plain markdown image.
  * Rewrite absolute docs.northbeam.io links to root-absolute preview paths (`/docs/*`, `/reference/*`).
  * Strip versioned prefixes (`/v2.2/docs/*` -> `/docs/*`).
  * Escape stray `<`/`>` and stray `{` sequences that acorn would misparse (conservative).
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

MIRROR = Path("/tmp/nb/mirror")
OUT = Path("/workspace")
DOCS_OUT = OUT / "docs"
REF_OUT = OUT / "reference"

CALLOUT_MAP = {
    "📘": "Note",
    "ℹ️": "Info",
    "ℹ": "Info",
    "💡": "Tip",
    "👍": "Tip",
    "✅": "Tip",
    "🚧": "Warning",
    "⚠️": "Warning",
    "⚠": "Warning",
    "❗️": "Warning",
    "❗": "Warning",
    "❌": "Warning",
    "📺": "Info",
    "🔔": "Info",
    "📌": "Info",
}

FRONTMATTER_RE = re.compile(r"^---\n.*?\n---\n", re.DOTALL)
BOILER_LINE_RE = re.compile(
    r"^Fetch the complete documentation index at:.*?before exploring further\.\s*$",
    re.MULTILINE,
)
BLOCK_IMAGE_RE = re.compile(r"\[block:image\]\s*(\{.*?\})\s*\[/block\]", re.DOTALL)
HTMLBLOCK_RE = re.compile(r"<HTMLBlock>\{`(.*?)`\}</HTMLBlock>", re.DOTALL)
IFRAME_RE = re.compile(r"<iframe([^>]*)>.*?</iframe>", re.DOTALL | re.IGNORECASE)


def yaml_escape(s: str) -> str:
    s = s.replace('"', "'").strip()
    # collapse whitespace
    s = re.sub(r"\s+", " ", s)
    return s


def convert_callouts(body: str) -> str:
    """Merge consecutive `> ` blockquote lines that start with an emoji into a Mintlify component."""
    lines = body.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^>\s*(" + "|".join(re.escape(k) for k in CALLOUT_MAP.keys()) + r")\s*(.*)$", line)
        if not m:
            out.append(line)
            i += 1
            continue
        emoji, first_rest = m.group(1), m.group(2)
        component = CALLOUT_MAP[emoji]
        content_lines: list[str] = []
        if first_rest.strip():
            content_lines.append(first_rest.rstrip())
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            if nxt.startswith(">"):
                stripped = nxt[1:].lstrip(" ")
                content_lines.append(stripped.rstrip())
                j += 1
            else:
                break
        # emit
        out.append(f"<{component}>")
        # keep an internal blank line between paragraphs
        for cl in content_lines:
            out.append("  " + cl if cl else "")
        out.append(f"</{component}>")
        # keep a blank line after the component
        if j < len(lines) and lines[j].strip() != "":
            out.append("")
        i = j
    return "\n".join(out)


def convert_html_blocks(body: str) -> str:
    def repl(m: re.Match) -> str:
        raw = m.group(1).strip()
        # find first iframe
        im = IFRAME_RE.search(raw)
        if im:
            attrs = im.group(1)
            # strip position style; keep src, width, height fallback
            src_m = re.search(r'src="([^"]+)"', attrs)
            if not src_m:
                return ""
            src = src_m.group(1)
            return f'<Frame>\n  <iframe src="{src}" width="100%" height="450" allowfullscreen></iframe>\n</Frame>'
        # fallback: strip block entirely
        return ""

    return HTMLBLOCK_RE.sub(repl, body)


def convert_block_image(body: str) -> str:
    def repl(m: re.Match) -> str:
        try:
            payload = json.loads(m.group(1))
        except Exception:
            return ""
        images = payload.get("images", [])
        out_parts = []
        for img in images:
            arr = img.get("image", [])
            if not arr:
                continue
            url = arr[0]
            alt = arr[1] if len(arr) > 1 else ""
            caption = arr[2] if len(arr) > 2 else ""
            block = f'<Frame'
            if caption:
                block += f' caption="{caption}"'
            block += f'>\n  <img src="{url}" alt="{alt or ""}" />\n</Frame>'
            out_parts.append(block)
        return "\n\n".join(out_parts)

    return BLOCK_IMAGE_RE.sub(repl, body)


LINK_RE = re.compile(r"\[([^\]]*)\]\((https?://docs\.northbeam\.io/[^\s)]+)\)")
BARE_URL_RE = re.compile(r"https?://docs\.northbeam\.io/(?:v[0-9.]+/)?(docs|reference)/([a-zA-Z0-9._-]+)(#[^\s)\]]+)?")

# Source docs frequently reference slugs that no longer exist or have been renamed.
# Remap the common ones so we don't ship broken links inherited from the source.
SLUG_REMAP: dict[str, str] = {
    "/docs/working-tracking-for-attentive-copy": "/docs/working-tracking-for-attentive",
    "/docs/setting-up-pinterest-ads-for-northbeam": "/docs/tracking-for-pinterest-ads",
    "/docs/tracking-for-bliss-point-media": "/docs/tracking-for-bliss-point-by-tinuiti",
    "/docs/northbeam-pixel": "/docs/add-pixel",
    "/docs/orders-api-1": "/docs/orders-api",
    "/docs/channel-tracking-overview": "/docs/all-other-platforms-overview",
    "/docs/clicks-views-enhanced": "/docs/clicks-deterministic-views",
    "/docs/setting-up-multiple-stores-or-regions": "/docs/adding-a-store-or-dashboard",
    "/reference/post_data-export": "/reference/post_data-export-1",
    "/docs/differences-in-total-revenue": "/docs/why-doesnt-northbeam-match-my-shopify-reporting",
    "/reference/spend": "/reference/post_spend",
    "/docs/setting-up-email-signups": "/docs/setting-up-klaviyo-for-northbeam",
    "/docs/purchase-pixel": "/docs/add-pixel",
    "/docs/correct-system-setups": "/docs/confirm-setup-requirements",
    "/docs/spend-api-1": "/docs/spend-api",
}


def apply_slug_remap(url: str) -> str:
    # Strip fragment before matching, restore after.
    frag = ""
    if "#" in url:
        base, frag = url.split("#", 1)
        frag = "#" + frag
    else:
        base = url
    if base.startswith("/update"):
        base = base[len("/update"):]
    base = SLUG_REMAP.get(base, base)
    return base + frag


def rewrite_links(body: str) -> str:
    def repl(m: re.Match) -> str:
        text, url = m.group(1), m.group(2)
        url2 = re.sub(r"^https?://docs\.northbeam\.io/(?:v[0-9.]+/)?", "/", url)
        url2 = re.sub(r"\.md(?=($|[?#]))", "", url2)
        if url2.endswith("/") and url2 != "/":
            url2 = url2.rstrip("/")
        url2 = apply_slug_remap(url2)
        return f"[{text}]({url2})"

    body = LINK_RE.sub(repl, body)

    def bare_repl(m: re.Match) -> str:
        kind, slug, frag = m.group(1), m.group(2), m.group(3) or ""
        slug = re.sub(r"\.md$", "", slug)
        return apply_slug_remap(f"/{kind}/{slug}") + frag
    body = BARE_URL_RE.sub(bare_repl, body)

    # Root-absolute internal links inserted by hand-written prose (already stripped domain)
    def local_repl(m: re.Match) -> str:
        text, url = m.group(1), m.group(2)
        return f"[{text}]({apply_slug_remap(url)})"
    body = re.sub(r"\[([^\]]*)\]\((/(?:docs|reference)/[^\s)]+)\)", local_repl, body)

    # Scheme-less markdown links pointing at bare hostnames
    def scheme_repl(m: re.Match) -> str:
        text, host = m.group(1), m.group(2)
        return f"[{text}](https://{host})"
    body = re.sub(
        r"\[([^\]]*)\]\((northbeam\.io/[A-Za-z0-9/_.\-]+|dashboard\.northbeam\.io)\)",
        scheme_repl,
        body,
    )

    # Relative sibling slug (`spend-api` -> `/docs/spend-api`) inside a `[](...)` link
    def sibling_repl(m: re.Match) -> str:
        text, slug = m.group(1), m.group(2)
        return f"[{text}](/docs/{slug})"
    body = re.sub(
        r"\[([^\]]*)\]\((?!https?:|/|#|mailto:|tel:)([a-z][a-z0-9\-]+(?:#[^)\s]*)?)\)",
        sibling_repl,
        body,
    )

    # Drop obvious placeholder images
    body = re.sub(
        r'<img src="YOUR_IMAGE_HERE"[^/>]*/>',
        "",
        body,
    )
    return body


EMAIL_AUTOLINK_RE = re.compile(r"<([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})\.?>")

CALLOUT_THEME = {
    "info": "Note",
    "default": "Info",
    "warn": "Warning",
    "warning": "Warning",
    "error": "Warning",
    "okay": "Tip",
    "success": "Tip",
}


def convert_readme_callouts(body: str) -> str:
    """Rewrite `<Callout icon="..." theme="...">...</Callout>` to a Mintlify component."""
    def repl(m: re.Match) -> str:
        attrs = m.group(1)
        inner = m.group(2)
        theme_m = re.search(r'theme="([a-z]+)"', attrs)
        theme = theme_m.group(1) if theme_m else "default"
        tag = CALLOUT_THEME.get(theme, "Info")
        return f"<{tag}>{inner}</{tag}>"
    return re.sub(
        r"<Callout([^>]*?)>(.*?)</Callout>", repl, body, flags=re.DOTALL,
    )



def _brace_replace(chunk: str) -> str:
    """Escape stray `{...}` in prose. Skip:
      - anything inside a JSX opening tag `<Word ...>` (its attribute-value braces are valid MDX),
      - explicit JSX expressions in a prop context (`attr={...}`).
    """
    out: list[str] = []
    i = 0
    n = len(chunk)
    in_tag = False
    while i < n:
        ch = chunk[i]
        # detect start of a JSX-ish tag `<A` where A is a letter
        if not in_tag and ch == "<" and i + 1 < n and (chunk[i + 1].isalpha() or chunk[i + 1] == "/"):
            in_tag = True
            out.append(ch)
            i += 1
            continue
        if in_tag:
            if ch == '"' or ch == "'":
                quote = ch
                out.append(ch)
                i += 1
                while i < n and chunk[i] != quote:
                    out.append(chunk[i])
                    i += 1
                if i < n:
                    out.append(chunk[i])
                    i += 1
                continue
            if ch == ">":
                in_tag = False
                out.append(ch)
                i += 1
                continue
            if ch == "{":
                depth = 1
                out.append(ch)
                i += 1
                while i < n and depth > 0:
                    if chunk[i] == "{":
                        depth += 1
                    elif chunk[i] == "}":
                        depth -= 1
                    out.append(chunk[i])
                    i += 1
                continue
            out.append(ch)
            i += 1
            continue
        if ch == "{":
            # already-escaped `\{` -> leave alone
            if i > 0 and chunk[i - 1] == "\\":
                out.append(ch)
                i += 1
                continue
            end = chunk.find("}", i + 1)
            nl = chunk.find("\n", i + 1)
            if end != -1 and (nl == -1 or end < nl) and (end - i) < 80:
                out.append("\\{")
                out.append(chunk[i + 1 : end])
                out.append("\\}")
                i = end + 1
                continue
        out.append(ch)
        i += 1
    return "".join(out)


def escape_stray_braces(body: str) -> str:
    """Escape `{...}` outside code fences / inline code / JSX attribute values."""
    parts: list[str] = []
    cursor = 0
    fence_re = re.compile(r"```.*?```|`[^`\n]*`", re.DOTALL)
    for m in fence_re.finditer(body):
        parts.append(_brace_replace(body[cursor:m.start()]))
        parts.append(m.group(0))
        cursor = m.end()
    parts.append(_brace_replace(body[cursor:]))
    return "".join(parts)


def _find_tag_end(body: str, start: int) -> int:
    """Given `<`, return index just past the closing `>` respecting quoted strings."""
    i = start + 1
    n = len(body)
    while i < n:
        c = body[i]
        if c == '"':
            j = body.find('"', i + 1)
            i = j + 1 if j != -1 else n
            continue
        if c == "'":
            j = body.find("'", i + 1)
            i = j + 1 if j != -1 else n
            continue
        if c == "{":
            depth = 1
            i += 1
            while i < n and depth > 0:
                if body[i] == "{":
                    depth += 1
                elif body[i] == "}":
                    depth -= 1
                i += 1
            continue
        if c == ">":
            return i + 1
        i += 1
    return n


def convert_anchor_tags(body: str) -> str:
    """Rewrite ReadMe `<Anchor href="..." ...>text</Anchor>` to markdown links."""
    def repl(m: re.Match) -> str:
        attrs = m.group(1)
        text = m.group(2).strip()
        href_m = re.search(r'href="([^"]+)"', attrs)
        if not href_m:
            return text
        # Strip stray autolink brackets inside the text
        text = re.sub(r"<(https?://[^>]+)>", r"\1", text)
        text = re.sub(r"^\s*<[^>]+>\s*$", "", text).strip() or href_m.group(1)
        return f"[{text}]({href_m.group(1)})"
    return re.sub(r"<Anchor([^>]*)>(.*?)</Anchor>", repl, body, flags=re.DOTALL)


def convert_readme_image_tags(body: str) -> str:
    """Rewrite ReadMe `<Image ... />` and `<Image ...>caption</Image>` to `<Frame><img/></Frame>`."""
    out: list[str] = []
    i = 0
    n = len(body)
    while i < n:
        if body.startswith("<Image", i) and i + 6 < n and body[i + 6] in " \t\n/>":
            tag_end = _find_tag_end(body, i)
            tag = body[i:tag_end]
            self_closing = tag.rstrip().endswith("/>")
            children = ""
            after = tag_end
            if not self_closing:
                close_idx = body.find("</Image>", tag_end)
                if close_idx != -1:
                    children = body[tag_end:close_idx].strip()
                    after = close_idx + len("</Image>")
            src_m = re.search(r'src="([^"]+)"', tag)
            alt_m = re.search(r'alt="([^"]*)"', tag)
            caption_m = re.search(r'caption="([^"]*)"', tag)
            caption = caption_m.group(1) if caption_m else children
            if src_m:
                frame = "<Frame"
                if caption:
                    cap = caption.replace('"', "'").replace("\n", " ").strip()
                    frame += f' caption="{cap}"'
                frame += (
                    f'>\n  <img src="{src_m.group(1)}" '
                    f'alt="{alt_m.group(1) if alt_m else ""}" />\n</Frame>'
                )
                out.append(frame)
            i = after
            continue
        out.append(body[i])
        i += 1
    return "".join(out)


def normalize_mdx_safety(body: str) -> str:
    body = re.sub(r"<((?:https?|mailto):[^>]+)>", r"\1", body)
    body = EMAIL_AUTOLINK_RE.sub(r"[\1](mailto:\1)", body)
    # Autolink of a bare root-absolute path: `</some/path>` -> plain URL
    # Require at least two path segments so we don't gobble closing JSX tags like </Warning>.
    body = re.sub(r"<(/[a-z0-9][a-z0-9_.\-]*/[A-Za-z0-9/_.\-#?=&%]+)>", r"\1", body)
    body = convert_readme_image_tags(body)
    return body


def extract_frontmatter_and_body(text: str) -> tuple[dict, str]:
    fm = {}
    m = FRONTMATTER_RE.match(text)
    if m:
        raw = m.group(0)
        for line in raw.split("\n"):
            line = line.strip()
            if not line or line == "---":
                continue
            if ":" in line:
                k, _, v = line.partition(":")
                fm[k.strip()] = v.strip()
        text = text[m.end():]
    text = BOILER_LINE_RE.sub("", text).lstrip("\n")
    return fm, text


H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


def extract_title_and_body(body: str) -> tuple[str, str, str | None]:
    m = H1_RE.search(body)
    if not m:
        return "", body, None
    title = m.group(1).strip()
    # remove exactly this H1 line
    start, end = m.start(), m.end()
    # skip blank lines after the H1
    after = body[end:].lstrip("\n")
    # Determine description: the first non-empty paragraph if it looks like a short lead (< 240 chars, single para)
    lead = None
    para_m = re.match(r"([^\n]+(?:\n[^\n]+)*)", after)
    if para_m:
        candidate = para_m.group(1).strip()
        # Only treat as lead if short-ish and not a heading / list / component / fence
        if (
            candidate
            and len(candidate) <= 240
            and "\n" not in candidate
            and not candidate.startswith(("#", "*", "-", "1.", "> ", "```", "<", "|"))
        ):
            lead = candidate
            after = after[para_m.end():].lstrip("\n")
    new_body = body[:start] + after
    return title, new_body, lead


def convert_file(src: Path, dst: Path) -> dict:
    raw = src.read_text(encoding="utf-8")
    fm_in, body = extract_frontmatter_and_body(raw)
    title, body, lead = extract_title_and_body(body)
    if not title:
        # derive from filename
        title = src.stem.replace("-", " ").title()
    body = convert_html_blocks(body)
    body = convert_block_image(body)
    body = convert_anchor_tags(body)
    body = convert_readme_callouts(body)
    body = convert_callouts(body)
    body = normalize_mdx_safety(body)
    body = rewrite_links(body)
    body = escape_stray_braces(body)
    # collapse >2 blank lines
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"

    fm_lines = ["---", f'title: "{yaml_escape(title)}"']
    if lead:
        fm_lines.append(f'description: "{yaml_escape(lead)}"')
    fm_lines.append("---\n\n")
    out = "\n".join(fm_lines) + body

    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(out, encoding="utf-8")
    return {"title": title, "description": lead, "path": str(dst.relative_to(OUT))}


def main():
    manifest = []
    for src in sorted((MIRROR / "docs").glob("*.md")):
        slug = src.stem
        dst = DOCS_OUT / f"{slug}.mdx"
        info = convert_file(src, dst)
        info["source_url"] = f"https://docs.northbeam.io/docs/{slug}"
        info["nav_section"] = "docs"
        manifest.append(info)
    for src in sorted((MIRROR / "reference").glob("*.md")):
        slug = src.stem
        dst = REF_OUT / f"{slug}.mdx"
        info = convert_file(src, dst)
        info["source_url"] = f"https://docs.northbeam.io/reference/{slug}"
        info["nav_section"] = "reference"
        manifest.append(info)
    (OUT / "parity-manifest.json").write_text(
        json.dumps({"pages": manifest}, indent=2), encoding="utf-8"
    )
    print(f"Converted {len(manifest)} pages")


if __name__ == "__main__":
    main()
