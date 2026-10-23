"""Lab 1 - Additional unit tests for basics.py."""
import pytest

from basics import gc_percent, parse_counts


def test_gc_percent_boundary_all_gc():
    """Boundary test: sequence composed entirely of G and C."""
    assert gc_percent(0, 50, 50, 0) == pytest.approx(100.0)


def test_gc_percent_zero_total_raises():
    """Zero total test: raising ValueError when count sum is zero."""
    with pytest.raises(ValueError):
        gc_percent(0, 0, 0, 0)


def test_parse_counts_invalid_input_raises():
    """Invalid input tests: negative values and insufficient elements."""
    with pytest.raises(ValueError):
        parse_counts("10 20 -5 15")
    with pytest.raises(ValueError):
        parse_counts("10 20 30")