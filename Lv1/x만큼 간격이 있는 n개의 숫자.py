def solution(x, n):
    return [i for i in range(x, x * (n + 1), x)] if x != 0 else [0] * n

assert(solution(2, 5) == [2,4,6,8,10])
assert(solution(4, 3) == [4,8,12])
assert(solution(-4, 2) == [-4,-8])