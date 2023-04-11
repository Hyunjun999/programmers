def solution(s):
    return s[len(s) // 2] if len(s) % 2 == 1 else s[len(s) // 2 - 1: len(s) // 2 + 1]

# Return the middle charater or string of the 's'. If the length of 's' is odd, return the middle character
# else return the 2 middle string

assert(solution('abcde') == 'c')
assert(solution('qwer') == 'we')