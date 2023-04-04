def solution(n):
    return sum([int(c) for c in str(n)])

assert(solution(123) == 6)
assert(solution(987) == 24)
assert(solution(789) == 24)