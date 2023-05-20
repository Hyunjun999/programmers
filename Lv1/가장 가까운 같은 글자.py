def solution(s):
    res = []
    for i in range(len(s)):
        if s[i] not in s[:i]:
            res.append(-1)
        elif s[i] in s[:i]:
            rev = s[:i][::-1]
            idx = 0
            for e in rev:
                if e == s[i]:
                    res.append(idx + 1)
                    break
                idx += 1
    return res
    # d = {}
    # for i in range(len(s)):
    #     if s[i] not in d:
    #         res.append(-1)
    #     else:
    #         res.append(i - d[s[i]])
    #     d[s[i]] = i

    # return res


# Find the letter that came out before me and has smallest distance with me,
# append each of letter's closest letter to the array to return it.

assert solution("banana") == [-1, -1, -1, 2, 2, 2]
assert solution("foobar") == [-1, -1, 1, -1, -1, -1]
