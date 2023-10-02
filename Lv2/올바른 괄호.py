def solution(s):
    l = []
    for char in s:
        if char == "(":
            l.append(char)
        elif len(l) == 0 or l.pop() != "(":
            return False
    return True if len(l) == 0 else False


# s consist of only open-parenthesis or close-parenthesis, return true if given s
# is right parenthesis

assert solution("(())()") == True
assert solution(")()(") == False
assert solution("(()(") == False
