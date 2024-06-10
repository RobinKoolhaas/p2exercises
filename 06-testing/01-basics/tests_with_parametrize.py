from intervals import overlapping_intervals
import pytest


@pytest.mark.parametrize('interval1, interval2', [
    ((1, 5), (4, 8)),
    ((4, 8), (1, 5)),
    ((2, 6), (3, 5)),
    ((3, 5), (2, 6)),
    ((1, 5), (1, 5))
])
def test_overlapping_intervals(interval1, interval2):
    assert overlapping_intervals(interval1, interval2) is True, f"Interval {interval1} overlaps with interval {interval2}"


@pytest.mark.parametrize('interval1, interval2', [
    ((1, 3), (4, 6)),
    ((4, 6), (1, 3)),
    ((5, 1), (3, 4)),
    ((3, 4), (5, 1)),
])
def test_non_overlapping_intervals(interval1, interval2):
    assert overlapping_intervals(interval1, interval2) is False, f"Interval {interval1} does not overlap with interval {interval2}"
