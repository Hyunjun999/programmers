def solution(s):
    ans = int(s[1:]) if s[0] == '+' else int(s)
    return ans

assert(solution("1234") == 1234)
assert(solution("-1234") == -1234)