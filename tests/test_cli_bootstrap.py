from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import research_system_javanese_profile_cli as cli



def test_prefer_local_src_moves_repo_src_to_front(monkeypatch) -> None:
    local_src = str(Path(cli.__file__).resolve().parent)
    monkeypatch.setattr(cli.sys, "path", ["D:/AI/src", local_src, "D:/other"])

    cli._prefer_local_src()

    assert cli.sys.path[0] == local_src
    assert cli.sys.path.count(local_src) == 1



def test_main_imports_profile_command(monkeypatch) -> None:
    calls: list[str] = []

    def fake_import_module(name: str) -> SimpleNamespace:
        calls.append(name)
        return SimpleNamespace(main=lambda: calls.append("main"))

    monkeypatch.setattr(cli, "import_module", fake_import_module)
    monkeypatch.setattr(cli, "_prefer_local_src", lambda: calls.append("prefer"))

    cli.main()

    assert calls == ["prefer", "research_system.commands.javanese_profile", "main"]
