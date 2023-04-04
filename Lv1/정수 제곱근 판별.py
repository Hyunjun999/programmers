def solution(n):
    num = 0
    if n == 1:
        return 4
    while num != n:
        if num * num == n:
            break
        num += 1
    else:
        return -1
    return (num + 1) ** 2