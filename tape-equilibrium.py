def solution(A):
    array_len = len(A)
    diff = [0] * array_len
    sum_left = 0
    sum_right = 0
    min_diff = 0
    for i in range(1, array_len):
        j = array_len - i
        sum_left += A[i - 1]
        sum_right += A[j]
        diff[i] += sum_left
        diff[j] -= sum_right
        if i == j:
            min_diff = abs(diff[i])
        elif i == j + 1:
            min_diff = min(abs(diff[i]), abs(diff[j]))
        elif i > j + 1:
            min_diff = min(min_diff, abs(diff[i]), abs(diff[j]))

    return min_diff

