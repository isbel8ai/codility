def solution(N):
    gap = 0
    counter = -1

    while N > 0:
        bit = int(N % 2)
        N = int((N - bit) / 2)
        if counter == -1:
            if bit == 1:
                counter = 0
        else:
            if bit == 0:
                counter += 1
            else:
                if counter > gap:
                    gap = counter
                counter = 0
                if N < 2 ** (gap + 1):
                    break
    return gap


num = 0b10011
print(bin(num))
print(solution(num))
