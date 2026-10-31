from collections.abc import Iterable, Iterator
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def read_events(lines: Iterable[str]) -> Iterator[dict[str, Any]]:
    """Yield parsed JSON event objects, skipping blank lines."""
    raise NotImplementedError("Complete lab 08")


def count_calls(function: F) -> F:
    """Decorate a function with a call_count attribute."""
    raise NotImplementedError("Complete lab 08")
