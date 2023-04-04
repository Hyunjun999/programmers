def solution(a, b):
    return sum([i for i in range(a, b + 1)]) if b > a  else sum([i for i in range(b, a + 1)])

# return sum of all numbers btw the parameters.

assert(solution(3, 5) == 12)
assert(solution(3, 3) == 3)
assert(solution(5, 3) == 12)
assert(solution(1, 10) == 55)