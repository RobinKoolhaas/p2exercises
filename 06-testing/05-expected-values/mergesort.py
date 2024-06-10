def split_in_two(ns: list) -> tuple:
    list_size = len(ns)
    return (ns[:list_size//2], ns[list_size//2:])


def merge_sorted(left: list, right: list) -> list:
    result = list()
    leftIndex = 0
    rightIndex = 0

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

    result.extend(left[leftIndex:])
    result.extend(right[rightIndex:])

    return result


def merge_sort(ns: list) -> list:
    if len(ns) <= 1:
        return ns

    left, right = split_in_two(ns)

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge_sorted(sorted_left, sorted_right)
