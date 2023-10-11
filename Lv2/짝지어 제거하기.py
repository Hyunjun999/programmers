def solution(s):
    stack = []

    for c in s:
        if len(stack) == 0:
            stack.append(c)
        elif stack[-1] != c:
            stack.append(c)
        elif stack[-1] == c:
            stack.pop()
    return 1 if len(stack) == 0 else 0


# Find the consecutive two alphabets and remove them in the string. Try to find another pair of alphabets
# in remained string to remove all characters completely.

assert solution("baabaa") == 1
assert solution("cdcd") == 0
