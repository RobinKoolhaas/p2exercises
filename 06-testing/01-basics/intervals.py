def overlapping_intervals(interval1, interval2):
    left1, right1 = interval1
    left2, right2 = interval2

    if left1 > right1:
        return False

    if left2 > right2:
        return False

    if left1 <= left2 <= right1:
        return True

    if left1 <= right2 <= right1:
        return True

    if left2 <= left1 <= right2:
        return True

    return False
