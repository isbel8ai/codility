def solution(N, A):
    major = 0
    counters = [0] * N
    for X in A:
        pos = X - 1
        if X <= N:
            counters[pos] += 1
            if counters[pos] > major:
                major = counters[pos]
        elif X == N + 1:
            counters = [major] * N

    return counters
