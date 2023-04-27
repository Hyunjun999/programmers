def solution(s):
    l, idx = list(s), 0 # Time complexity = O(n)
    for i in range(len(s)):
        if s[i].isalpha():
            if idx % 2 == 0:
                l[i] = s[i].upper()
            else:
                l[i] = s[i].lower()
            idx += 1
        else: 
            idx = 0
    return ''.join(l)

    # res = '' # Time Complexity = O(n^2)
    # for w in s.split(' '):
    #     for i, c in enumerate(w):
    #         if i % 2 == 0:
    #             res += c.upper()
    #         else:
    #             res += c.lower()
    #     res += ' '
    # return res[:-1]

# Change the character which has the even index based on the word, but we the index
# ,here, does consider the 'space'

assert(solution("try hello world") == "TrY HeLlO WoRlD")
assert(solution("aaa bbb    ccc") == "AaA BbB    CcC")