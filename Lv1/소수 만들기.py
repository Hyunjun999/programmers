def solution(nums):
    prime = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if isPrime(nums[i] + nums[j] + nums[k]):
                    prime += 1
    return prime


def isPrime(n):
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True


# Try to get the number of cases that 3 choosed numbers' sum from nums is prime or not

assert solution([1, 2, 3, 4]) == 1  # can make 7
assert solution([1, 2, 7, 6, 4]) == 4  # can make 7, 11, 13, 17
