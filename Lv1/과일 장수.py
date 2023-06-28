def solution(k, m, score):
    res = 0
    score.sort(reverse=True)
    rem = len(score) % m
    s = score[: len(score) - rem]
    for i in range(0, len(s), m):
        l = score[i : i + m]
        res += min(l) * m
    return res


assert solution(3, 4, [1, 2, 3, 1, 2, 3, 1]) == 8
assert solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]) == 33
