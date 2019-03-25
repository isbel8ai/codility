def solution(A):
    singles = {}
    for num in A:
        try:
            singles.pop(num)
        except KeyError:
            singles[num] = True

    return singles.popitem()[1]

