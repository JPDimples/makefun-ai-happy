#!/usr/bin/env python3
"""ai-happy-01 entry: copy the bundled happy image to /output/entry.png.

Deterministic, standard library only, no network. The image is the
entry.png file beside this script (JPEG bytes, 1024x683, 216491 bytes).
Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
from pathlib import Path


def main():
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve().parent / "entry.png"
    if not src.is_file():
        raise FileNotFoundError(f"entry image missing: {src}")
    if src.stat().st_size > 1048576:
        raise ValueError("entry image is over the 1 MiB limit")
    dest = out / "entry.png"
    shutil.copyfile(src, dest)
    if dest.stat().st_size != src.stat().st_size:
        raise ValueError("copied entry image differs from the source")


if __name__ == "__main__":
    main()
