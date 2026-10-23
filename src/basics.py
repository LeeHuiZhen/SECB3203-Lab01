"""Lab 1 - Python fundamentals for biological calculations."""


def gc_percent(a: int, c: int, g: int, t: int) -> float:
    """Return the GC percentage from the four base counts.

    Raises:
        ValueError: if any count is negative or the total is zero.
    """
    if min(a, c, g, t) < 0:
        raise ValueError("base counts must not be negative")
    total = a + c + g + t
    if total == 0:
        raise ValueError("total base count is zero")
    return (g + c) / total * 100


def format_report(sample: str, length: int, gc: float) -> str:
    """Return a one-line report with units, e.g. 'S1: 60 bases, GC 46.7%'."""
    return f"{sample}: {length} bases, GC {gc:.1f}%"


def parse_counts(text: str) -> tuple[int, int, int, int]:
    """Parse 'A C G T' counts separated by spaces or commas.

    Raises:
        ValueError: if there are not exactly four non-negative integers.
    """
    parts = text.replace(",", " ").split()
    if len(parts) != 4:
        raise ValueError(
            f"expected four counts (A C G T), got {len(parts)}: {text!r}"
        )
    try:
        a, c, g, t = (int(p) for p in parts)
    except ValueError as err:
        raise ValueError(
            f"counts must be whole numbers: {text!r}"
        ) from err

    if min(a, c, g, t) < 0:
        raise ValueError("base counts must not be negative")
    return a, c, g, t


if __name__ == "__main__":
    a, c, g, t = parse_counts("24, 42 46 29")
    gc = gc_percent(a, c, g, t)
    print(format_report("ISO_001", a + c + g + t, gc))
