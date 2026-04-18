#!/usr/bin/env python3
"""Download a set of Markdown files from code.claude.com and save them into a new folder.

Usage: python3 scripts/download_claude_docs.py
"""
import os
import sys
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

URLS = [
    "https://code.claude.com/docs/en/agent-sdk/overview.md",
    "https://code.claude.com/docs/en/sub-agents.md",
    "https://code.claude.com/docs/en/agent-teams.md",
    "https://code.claude.com/docs/en/skills.md",
    "https://code.claude.com/docs/en/plugins.md",
    "https://code.claude.com/docs/en/plugins-reference.md",
    "https://code.claude.com/docs/en/how-claude-code-works.md",
    "https://code.claude.com/docs/en/features-overview.md",
    "https://code.claude.com/docs/en/claude-directory.md",
    "https://code.claude.com/docs/en/context-window.md",
    "https://code.claude.com/docs/en/memory.md",
    "https://code.claude.com/docs/en/common-workflows.md",
    "https://code.claude.com/docs/en/best-practices.md",
    "https://code.claude.com/docs/en/channels.md",
    "https://code.claude.com/docs/en/cli-reference.md",
    "https://code.claude.com/docs/en/common-workflows.md",
    "https://code.claude.com/docs/en/costs.md",
    "https://code.claude.com/docs/en/discover-plugins.md",
    "https://code.claude.com/docs/en/errors.md",
    "https://code.claude.com/docs/en/features-overview.md",
    "https://code.claude.com/docs/en/headless.md",
    "https://code.claude.com/docs/en/hooks.md",
    "https://code.claude.com/docs/en/hooks-guide.md",
    "https://code.claude.com/docs/en/interactive-mode.md",
    "https://code.claude.com/docs/en/mcp.md",
    "https://code.claude.com/docs/en/overview.md",
    "https://code.claude.com/docs/en/permissions.md",
    "https://code.claude.com/docs/en/scheduled-tasks.md",
    "https://code.claude.com/docs/en/settings.md",
    "https://code.claude.com/docs/en/setup.md",
    "https://code.claude.com/docs/en/third-party-integrations.md",
    "https://code.claude.com/docs/en/troubleshooting.md",
]

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "CLAUDE_DOCS")

def safe_filename(url: str) -> str:
    # use last path segment as filename
    name = url.rstrip('/').split('/')[-1]
    if not name:
        name = url.replace('https://', '').replace('/', '_')
    return name

def download(url: str) -> bytes:
    headers = {"User-Agent": "curl/7.64.1"}
    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=30) as resp:
            return resp.read()
    except HTTPError as e:
        print(f"HTTP error for {url}: {e.code} {e.reason}")
    except URLError as e:
        print(f"URL error for {url}: {e.reason}")
    except Exception as e:
        print(f"Unexpected error for {url}: {e}")
    return b""

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    saved = []
    for url in URLS:
        print(f"Downloading: {url}")
        content = download(url)
        if not content:
            print(f"Failed to download: {url}")
            continue
        fname = safe_filename(url)
        path = os.path.join(OUT_DIR, fname)
        try:
            with open(path, 'wb') as f:
                f.write(content)
            saved.append(path)
            print(f"Saved: {path}")
        except Exception as e:
            print(f"Failed to save {path}: {e}")

    # write index
    idx_path = os.path.join(OUT_DIR, 'INDEX.md')
    with open(idx_path, 'w', encoding='utf-8') as idx:
        idx.write('# Claudë Docs Index\n\n')
        for p in saved:
            idx.write(f"- {os.path.basename(p)}\n")

    print(f"Done. Files saved to: {OUT_DIR}")

if __name__ == '__main__':
    main()
