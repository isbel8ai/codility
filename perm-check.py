def solution(A):
    array_len = len(A)
    present = [False] * array_len

    for num in A:
        if num < 1:
            return 0
        if num > array_len:
            return 0
        if present[num - 1]:
            return 0
        present[num - 1] = True

    return 1
