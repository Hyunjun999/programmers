def solution(n):
    answer = 0
    for i in range(1, n + 1):
        s = 0
        while s < n:
            s += i
            i += 1
        if s == n:
            answer += 1
    return answer


# n is a target number can be made by consecutive numbers' sum. Return the number of ways to be
# the target number. For example, 15 can be expressed like 1 + 2 + 3 + 4 + 5 = 15, 4 + 5 + 6 = 15, 7 + 8 = 15, 15 = 15
# Thus return 4

assert solution(15) == 4
