def solution(k, score):
    q, res = [], []
    for s in score:
        if len(q) < k:
            q.append(s)
            q.sort()
            res.append(q[0])
        else:
            if q[0] < s:
                q.remove(q[0])
                q.append(s)
                q.sort()
                res.append(q[0])
                continue
            res.append(q[0])
    return res


# Scoreboard can notify only 'k' number of score from the score array.

assert solution(3, [10, 100, 20, 150, 1, 100, 200]) == [10, 10, 10, 20, 20, 100, 100]
assert solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]) == [
    0,
    0,
    0,
    0,
    20,
    40,
    70,
    70,
    150,
    300,
]
