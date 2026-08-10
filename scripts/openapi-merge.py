#!/usr/bin/env python3
"""Extract inline ReadMe OpenAPI fragments from each reference/*.mdx,
merge them into one spec per product (openapi/*.json), and rewrite each
reference page to overlay the playground via per-page frontmatter.

Follows mstack docs-to-mintlify → openapi.md → "Hand-migrated endpoint pages + a spec".
"""
from __future__ import annotations

import copy
import json
import os
import re
from pathlib import Path

ROOT = Path("/workspace")
REF_DIR = ROOT / "reference"
OPENAPI_DIR = ROOT / "openapi"
OPENAPI_DIR.mkdir(exist_ok=True)

FENCE_RE = re.compile(r"```json\s*\n(\{.*?\n\})\s*\n```", re.DOTALL)
H1_OPENAPI_RE = re.compile(r"^#\s+OpenAPI definition\s*\n", re.MULTILINE)
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

# Sanitized filenames per API title
API_MAP = {
    "API - Orders - V1 (Deprecated)": "orders-v1",
    "API - Orders - V2": "orders-v2",
    "API - Spend - V1": "spend-v1",
    "API - DATA EXPORT - V1": "data-export-v1",
}

specs: dict[str, dict] = {}
page_operation: dict[str, tuple[str, str, str]] = {}  # slug -> (spec_key, method, path)


def clean_numeric_strings(node):
    """ReadMe embeds `maximum: '100_000_000_000_000'` which isn't valid OAS.
    Recursively coerce string-encoded numerics on the numeric-valued keys."""
    NUMERIC_KEYS = {"maximum", "minimum", "exclusiveMinimum", "exclusiveMaximum", "multipleOf"}
    if isinstance(node, dict):
        for k, v in list(node.items()):
            if k in NUMERIC_KEYS and isinstance(v, str):
                try:
                    node[k] = float(v.replace("_", "")) if "." in v else int(v.replace("_", ""))
                except ValueError:
                    pass
            else:
                clean_numeric_strings(v)
    elif isinstance(node, list):
        for item in node:
            clean_numeric_strings(item)


for mdx_path in sorted(REF_DIR.glob("*.mdx")):
    slug = mdx_path.stem
    text = mdx_path.read_text(encoding="utf-8")
    m = FENCE_RE.search(text)
    if not m:
        print(f"skip {slug}: no JSON fence")
        continue
    try:
        frag = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        print(f"skip {slug}: invalid JSON ({e})")
        continue
    clean_numeric_strings(frag)
    title = frag.get("info", {}).get("title", "unknown")
    spec_key = API_MAP.get(title, re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-"))
    if spec_key not in specs:
        specs[spec_key] = copy.deepcopy(frag)
        # ensure containers
        specs[spec_key].setdefault("paths", {})
        specs[spec_key].setdefault("components", {})
        specs[spec_key]["components"].setdefault("schemas", {})
        specs[spec_key]["components"].setdefault("securitySchemes", {})
        specs[spec_key].setdefault("tags", [])
    dst = specs[spec_key]
    # merge components.schemas
    for sch_name, sch in frag.get("components", {}).get("schemas", {}).items():
        dst["components"]["schemas"].setdefault(sch_name, sch)
    for ss_name, ss in frag.get("components", {}).get("securitySchemes", {}).items():
        dst["components"]["securitySchemes"].setdefault(ss_name, ss)
    for t in frag.get("tags", []):
        if t not in dst["tags"]:
            dst["tags"].append(t)
    # merge paths + record the operation for this page
    for p, ops in frag.get("paths", {}).items():
        dst["paths"].setdefault(p, {})
        for method, op in ops.items():
            if method.lower() in ("get", "post", "put", "patch", "delete", "options", "head"):
                dst["paths"][p][method] = op
                page_operation[slug] = (spec_key, method.lower(), p)
    # servers/security -> keep the first-encountered
    if "servers" not in dst or not dst["servers"]:
        dst["servers"] = frag.get("servers", [])

# write specs
for key, spec in specs.items():
    out = OPENAPI_DIR / f"{key}.json"
    out.write_text(json.dumps(spec, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out} ({len(spec['paths'])} paths)")

# rewrite reference pages
for mdx_path in sorted(REF_DIR.glob("*.mdx")):
    slug = mdx_path.stem
    text = mdx_path.read_text(encoding="utf-8")
    fm_m = FRONTMATTER_RE.match(text)
    fm_body = fm_m.group(1) if fm_m else ""
    body = text[fm_m.end():] if fm_m else text

    # strip the "# OpenAPI definition" heading and the following json fence
    body = H1_OPENAPI_RE.sub("", body)
    body = FENCE_RE.sub("", body, count=1)
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"

    op = page_operation.get(slug)
    if op:
        spec_key, method, path = op
        openapi_line = f'openapi: "openapi/{spec_key}.json {method.upper()} {path}"'
        # inject openapi: field into frontmatter (dedupe first)
        fm_lines = [ln for ln in fm_body.split("\n") if not ln.startswith("openapi:")]
        fm_lines.append(openapi_line)
        new_fm = "\n".join(fm_lines).strip()
        text_out = f"---\n{new_fm}\n---\n\n{body}"
    else:
        text_out = f"---\n{fm_body}\n---\n\n{body}"
    mdx_path.write_text(text_out, encoding="utf-8")

print(f"rewrote {len(list(REF_DIR.glob('*.mdx')))} reference pages")
