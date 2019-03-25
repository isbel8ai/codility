def solution(A):
    present = {}
    for num in A:
        present[num] = True

    result = 1
    while present.get(result):
        result += 1

    return result
