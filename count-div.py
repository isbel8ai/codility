def solution(A, B, K):
    diff = B - A
    count = int(diff / K)
    rest_A = A % K
    rest_B = B % K
    rest_diff = diff % K
    if rest_diff == 0:
        if rest_A == 0:
            return count + 1
        else:
            return count
    else:
        if rest_A == 0 or rest_B == 0:
            return count + 1
        else:
            if K - rest_A + rest_B > K:
                return count
            else:
                return count + 1
