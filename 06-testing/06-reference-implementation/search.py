def linear_search(students: list, target_id: int) -> any:
    for student in students:
        if student.id == target_id:
            return student

    return None


def binary_search(students: list, target_id: int) -> any:
    left = 0
    right = len(students)

    while left < right:
        middle = (left + right) // 2
        middle_id = students[middle].id

        if target_id < middle_id:
            right = middle
        elif target_id > middle_id:
            left = middle + 1
        else:
            return students[middle]
    return None
