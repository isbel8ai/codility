def solution(X, Y, D):
    distance = Y - X
    if distance == 0:
        return 0

    return int(distance / D) + (0 if distance % D == 0 else 1)
