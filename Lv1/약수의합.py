def solution(n):
    return sum([i for i in range(1, n + 1) if n % i == 0])

assert(solution(12) == 28)
assert(solution(5) == 6)