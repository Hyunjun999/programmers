def solution(s):
    return s.isdigit() if len(s) == 4 or len(s) == 6 else False

assert(solution("a234") == False)
assert(solution('1234') == True)