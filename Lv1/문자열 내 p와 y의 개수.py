def solution(s):
    words = s.lower()
    p_num = 0
    y_num = 0
    for char in words:
        if char == 'p':
            p_num += 1
        elif char == 'y':
            y_num += 1
    return True if p_num == y_num else False

assert(solution("pPoooyY") == True)
assert(solution("Pyy") == False)
# return True if the # of p and # of y in given s are same 
# regardless of they are capital or lower letter, or return False
