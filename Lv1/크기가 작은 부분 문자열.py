def solution(t, p):
    # l = []
    # for i in range(len(t) - len(p) + 1):
    #     l.append(t[i : i + len(p)])
    return len(
        list(
            filter(
                lambda x: int(x) <= int(p),
                [t[i : i + len(p)] for i in range(len(t) - len(p) + 1)],
            )
        )
    )


# In the substrings of 't' which have the same length of 'p', return how many elements that
# they are smaller than or equal to the 'p'

assert solution("3141592", "271") == 2
assert solution("500220839878", "7") == 8
assert solution("10203", "15") == 3
