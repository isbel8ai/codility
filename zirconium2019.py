def sum_range(array, cache, count, offset):
    if offset == len(array):
        return 0

    if cache[count][offset] == -1:
        cache[count][offset] = array[offset] + sum_range(array, cache, count, offset + 1)

    return cache[count][offset]


def max_contribution(count, offset, target, other, cache):
    if cache[count][offset] != -1:
        return cache[count][offset]

    if count == 0:
        return sum_range(other, cache, 0, offset)

    if count == len(target) - offset:
        return sum_range(target, cache, count, offset)

    in_target = target[offset] + max_contribution(count - 1, offset + 1, target, other, cache)
    in_other = other[offset] + max_contribution(count, offset + 1, target, other, cache)

    cache[count][offset] = max(in_target, in_other)
    return cache[count][offset]


def solution(A, B, F):
    N = len(A)
    G = N - F

    if F < G:
        cache = [[-1] * N for i in range(F + 1)]
        return max_contribution(F, 0, A, B, cache)
    else:
        cache = [[-1] * N for i in range(G + 1)]
        return max_contribution(G, 0, B, A, cache)


print(solution([4, 2, 1], [2, 5, 3], 2))
print(solution([5, 5, 5], [5, 5, 5], 1))
print(solution([7, 1, 4, 4], [5, 3, 4, 3], 2))
