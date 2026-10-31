from pathlib import Path


def load_notes(path: Path) -> list[str]:
    """Load JSON notes; return an empty list if the file does not exist."""
    raise NotImplementedError("Complete lab 05")


def save_notes(path: Path, notes: list[str]) -> None:
    """Save notes as JSON, creating parent directories if needed."""
    raise NotImplementedError("Complete lab 05")
