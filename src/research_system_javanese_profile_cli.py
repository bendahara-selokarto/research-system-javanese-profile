from __future__ import annotations

from importlib import import_module
from pathlib import Path
import sys


def _prefer_local_src() -> None:
    local_src = str(Path(__file__).resolve().parent)
    while local_src in sys.path:
        sys.path.remove(local_src)
    sys.path.insert(0, local_src)


def main() -> None:
    _prefer_local_src()
    import_module("research_system.commands.javanese_profile").main()
