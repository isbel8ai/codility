def solution(A):
    max_depth = -1
    n = len(A)
    p = 0
    while p < n - 3:
        q = p
        while A[q] > A[q + 1] and q < n - 2:
            q += 1

        if q == p:
            p += 1
            continue

        diff_pq = A[p] - A[q]
        if diff_pq <= max_depth:
            p = q
            continue

        r = q
        while A[r] < A[r + 1] and A[r] - A[q] < diff_pq and r < n - 1:
            r += 1

        if r == q:
            p = q
            continue

        diff_rq = A[r] - A[q]
        if diff_rq > max_depth:
            max_depth = min(diff_pq, diff_rq)

        p = r

    return max_depth
