# Lab 08: Advanced Python building blocks

**Learn:** type hints, iterators, generators, decorators, and context managers.

**Task:** implement `read_events(lines)` as a generator that parses JSON lines into dictionaries, skips blank lines, and reports malformed line numbers with `ValueError`. Implement a decorator `count_calls` that preserves the wrapped function metadata and exposes its call count. Use both in a log analyzer that processes large files without loading them all into memory.

**Done when:** parsing is lazy, malformed records identify their line, the decorator counts calls, and tests cover empty input and multiple records.
