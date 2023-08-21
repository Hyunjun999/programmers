def solution(n, m, section):
    res = 0
    p = section[0] - 1
    for s in section:
        if p < s:
            p = s + m - 1
            res += 1
    return res


# n is a total width of the wall and section contains specific parts where it needs to be
# re-painted. Given the m which denotes available length roller can cover, return the
# minimum repeats to paint with the roller
