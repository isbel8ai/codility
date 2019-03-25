def solution(A):
    mapping = {}
    for i in range(1, len(A) + 2):
        mapping[i] = True

    for key in A:
        mapping.pop(key)

    return mapping.popitem()[0]
