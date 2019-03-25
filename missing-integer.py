def solution(A):
    present = {}
    for num in A:
        present[num] = True

    smaller = 1
    while present.get(smaller):
        smaller += 1

    return smaller


print(solution([1, 3, 6, 4, 1, 2]))
