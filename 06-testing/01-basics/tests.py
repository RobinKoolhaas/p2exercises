from intervals import overlapping_intervals


def test_overlapping_intervals():
    assert overlapping_intervals((1, 5), (4, 8)) is True
    assert overlapping_intervals((4, 8), (1, 5)) is True
    assert overlapping_intervals((2, 6), (3, 5)) is True
    assert overlapping_intervals((3, 5), (2, 6)) is True
    assert overlapping_intervals((1, 5), (1, 5)) is True

    assert overlapping_intervals((1, 3), (4, 6)) is False
    assert overlapping_intervals((4, 6), (1, 3)) is False

    assert overlapping_intervals((5, 1), (3, 4)) is False
    assert overlapping_intervals((3, 4), (5, 1)) is False
