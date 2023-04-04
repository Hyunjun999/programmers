def solution(n):
    return min(list(filter(lambda x: n % x == 1, map(int, [i for i in range(1, n)]))))

assert(solution(10) == 3)
assert(solution(12) == 11)

# Find the smallest number that has remain as 1, after n divides with the number