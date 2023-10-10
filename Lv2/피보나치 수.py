def solution(n):
    fib = [0, 1]
    index = 2
    while index != n + 1:
        fib.append(fib[index - 1] + fib[index - 2])
        index += 1
    return fib[-1] % 1234567


# Return the remainder of n-th fibonacci number divided by 1234567

assert solution(3) == 2
assert solution(5) == 5
