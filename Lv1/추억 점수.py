def solution(name, yearning, photo):
    ans = []
    d = dict(zip(name, yearning))
    for p in photo:
        score = 0
        for e in p:
            if e in d:
                score += d[e]
        ans.append(score)
    return ans


# Append the sum of score that we see the each line at the photo,

assert solution(
    ["may", "kein", "kain", "radi"],
    [5, 10, 1, 3],
    [
        ["may", "kein", "kain", "radi"],
        ["may", "kein", "brin", "deny"],
        ["kon", "kain", "may", "coni"],
    ],
) == [19, 15, 6]

assert solution(
    ["kali", "mari", "don"],
    [11, 1, 55],
    [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]],
) == [67, 0, 55]

assert solution(
    ["may", "kein", "kain", "radi"],
    [5, 10, 1, 3],
    [["may"], ["kein", "deny", "may"], ["kon", "coni"]],
) == [5, 15, 0]
