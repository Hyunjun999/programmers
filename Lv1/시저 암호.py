def solution(s, n):
    res = ''
    for c in s:
        if c == ' ':
            res += ' '
        elif 97 <= ord(c) <= 122:
            if ord(c) + n > 122:
                res += chr(ord(c) + n - 26)
            else:
                res += chr(ord(c) + n)
        elif 65 <= ord(c) <= 90:
            if ord(c) + n > 90:
                res += chr(ord(c) + n - 26)
            else:
                res += chr(ord(c) + n)
    return res

# With the given string, s and n which means how many we are going to push, return
# the encoded string. Actually this encryption is called 'Caesar cipher'

assert(solution("AB", 1) == "BC")
assert(solution('z', 1) == 'a')
assert(solution('a B z', 4) == 'e F d')