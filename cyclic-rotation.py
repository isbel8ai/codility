def solution(A, K):
    array_len = len(A)
    if array_len < 2:
        return A
    offset = K % array_len
    if offset == 0:
        return A

    if offset > array_len - offset:
        offset = K - array_len

    result = []
    for pos, val in enumerate(A):
        result.append(A[(pos - offset) % array_len])

    return result








