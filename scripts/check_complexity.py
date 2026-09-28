#!/usr/bin/env python3
"""Fail if any function exceeds McCabe complexity 10 (ruff C901)."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    cmd = [sys.executable, "-m", "ruff", "check", "src", "scripts", "--select", "C901"]
    result = subprocess.run(cmd, cwd=ROOT, check=False)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
