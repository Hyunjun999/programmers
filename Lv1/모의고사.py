def solution(answers):
    corr = []
    a = list(range(1, 6))
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for e in [a, b, c]:
        ans = 0
        quo, rem = divmod(len(answers), len(e))
        for i, j in zip(answers, e * quo + e[:rem]):
            if i == j:
                ans += 1
        corr.append(ans)
    res = []
    if corr.count(max(corr)) > 1:
        for i in range(len(corr)):
            if corr[i] == max(corr):
                res.append(i + 1)
        return res
    else:
        res.append(corr.index(max(corr)) + 1)
        return res


assert solution([1, 2, 3, 4, 5]) == [1]
assert solution([1, 3, 2, 4, 2]) == [1, 2, 3]
