# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `src/pybookmarks/main.py:13` - the only endpoint is `show_accounts`, which dumps Chrome's profile cache; nothing reads, manages or syncs bookmarks, yet `config/project.lua:2` (and so `pyproject.toml:16` and the README) describe a "Book mark manager and sync between browsers" with keywords `firefox`, `bookmarks`, `html`, and `pyproject.toml:27` claims "Development Status :: 4 - Beta". Either implement bookmark reading (Chrome `Bookmarks` JSON / Firefox `places.sqlite`) or describe the tool as it is and use "2 - Pre-Alpha".
- `src/pybookmarks/utils.py:9` - `get_accounts()` hardcodes `~/.config/google-chrome/Local State` and lets a missing file (no Chrome, Chromium, or macOS) escape as a raw `FileNotFoundError` traceback / `KeyError` for an unexpected layout; catch these and print a clear error, and open the file with `encoding="utf-8"`.
- `rsconstruct.toml:28` - ruff and mypy (`:32`) list `config`, which holds only Lua files; use `src_dirs = ["src", "tests"]`.

## Low

- `pyproject.toml:81` - `mypy_path = "src:python:scripts"` names `python/` and `scripts/`, which do not exist in this repo; use `"src"`.
- `pyproject.toml:101` - `pylogconf` and `pytconf` are repeated in the `dev` group although they are already runtime `dependencies` (`pyproject.toml:37`); drop them from `dev`.
- `src/pybookmarks/utils.py:8` - `get_accounts()` has no return annotation (and `main()` at `src/pybookmarks/main.py:25` none either); add `-> dict[str, Any]` / `-> None` so mypy actually checks the callers.
- `doc/TODO.txt:1` - empty file; delete it.
