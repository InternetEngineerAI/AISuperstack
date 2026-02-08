#!/usr/bin/env python3
"""
download_subtitles.py
Downloads YouTube subtitles to a local .srt file (start/end time included).
Output filename includes the YouTube video ID.

Requires: pip install -U yt-dlp
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path


YOUTUBE_ID_RE = re.compile(r"(?:v=|/shorts/|youtu\.be/)([A-Za-z0-9_-]{11})")


def extract_youtube_id(url: str) -> str:
    m = YOUTUBE_ID_RE.search(url)
    if not m:
        raise ValueError(f"Could not extract a YouTube ID from: {url}")
    return m.group(1)


def ensure_tool(name: str) -> None:
    if shutil.which(name) is None:
        raise RuntimeError(
            f"Missing '{name}' on PATH. Install it or ensure it's available.\n"
            f"If you installed yt-dlp via pip, try: python -m pip install -U yt-dlp"
        )


def download_srt(
    url: str,
    out_dir: str | Path = ".",
    lang: str = "en",
    prefer_manual: bool = True,
) -> Path:
    """
    Downloads subtitles as SRT to out_dir.
    The output file name will be: <video_id>.<lang>.srt  (or similar depending on availability)
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    video_id = extract_youtube_id(url)

    ensure_tool("yt-dlp")

    # yt-dlp output template:
    # - %(id)s ensures the filename includes the YouTube ID
    # - %(language)s uses subtitle language code
    # - We'll force conversion to srt when possible
    outtmpl = str(out_dir / "%(id)s.%(language)s.%(ext)s")

    cmd = [
        "yt-dlp",
        "--skip-download",
        "--write-subs",
        "--sub-langs",
        lang,
        "--convert-subs",
        "srt",
        "--output",
        outtmpl,
        url,
    ]

    if not prefer_manual:
        # If you ONLY want auto-captions, use this and remove --write-subs
        # cmd[cmd.index("--write-subs")] = "--write-auto-subs"
        pass
    else:
        # Try manual subs first; if not present, we’ll fall back to auto subs.
        # We'll run once for manual subs; if nothing was written, run auto.
        pass

    # 1) Try manual subs
    manual = cmd.copy()
    # (manual already has --write-subs)
    subprocess.run(manual, check=True)

    # If manual subs weren't available, yt-dlp may not create a file.
    # We’ll check for any file starting with <video_id>. in the output dir.
    candidates = sorted(out_dir.glob(f"{video_id}.*.srt"))
    if candidates:
        return candidates[0]

    # 2) Fall back to auto subs
    auto_cmd = [
        "yt-dlp",
        "--skip-download",
        "--write-auto-subs",
        "--sub-langs",
        lang,
        "--convert-subs",
        "srt",
        "--output",
        outtmpl,
        url,
    ]
    subprocess.run(auto_cmd, check=True)

    candidates = sorted(out_dir.glob(f"{video_id}.*.srt"))
    if not candidates:
        raise RuntimeError(
            f"No subtitles found for video {video_id} (lang={lang}). "
            f"Try a different language code or check if captions exist."
        )
    return candidates[0]


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python download_subtitles.py <youtube_url> [lang] [out_dir]")
        return 2

    url = sys.argv[1]
    lang = sys.argv[2] if len(sys.argv) > 2 else "en"
    out_dir = sys.argv[3] if len(sys.argv) > 3 else "."

    out_path = download_srt(url=url, out_dir=out_dir, lang=lang)
    print(f"Saved subtitles to: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
