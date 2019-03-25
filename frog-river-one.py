def solution(X, A):
    array_len = len(A)
    if array_len < X:
        return -1
    min_pos_time = [array_len] * X
    for time, pos in enumerate(A):
        min_pos_time[pos - 1] = min(min_pos_time[pos - 1], time)

    earlier = 0
    for time in min_pos_time:
        if time == array_len:
            return -1
        earlier = max(time, earlier)

    return earlier
