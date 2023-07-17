def solution(n):
    l = [i for i in range(2, n + 1)]
    ans = list(filter(lambda x: isPrime(x), l))
    return len(ans)


def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Return
