def solution(A):
    N = len(A)
    zeros = 0
    result = 0
    for car in A:
        if car == 0:
            zeros += 1
        else:
            result += zeros
            if result > 1000000000:
                return -1

    return result
