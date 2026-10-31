# Lab 05: Files and errors

**Learn:** `pathlib`, JSON, exceptions, and safe file handling.

**Task:** implement `load_notes(path)` and `save_notes(path, notes)` in `starter.py`. Persist a list of strings as JSON. A missing file loads as an empty list. Invalid JSON should raise a clear `ValueError`; do not silently discard data. Build a notes CLI with add, list, and delete actions.

**Done when:** data survives a restart, a missing file is handled, and malformed JSON produces a useful error. Use a temporary directory in tests.
