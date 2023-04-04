def solution(num):
    time = 1
    if num == 1:
        return 0
    while time <= 500:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        if num == 1:
            return time
        time += 1
    return -1

# Collatz conjecture is how many times we need to make the number as 1. 
# If the number is even, it should be halved, 
# else will be multiplied by 3 and added by 1

assert(solution(6) == 8)
assert(solution(16) == 4)
assert(solution(626331) == -1)