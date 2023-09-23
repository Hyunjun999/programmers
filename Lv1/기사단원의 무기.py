def solution(number, limit, power):
    div = []
    for n in range(1, number + 1):
        cnt = 0
        for i in range(1, int(n**0.5) + 1):
            if n / i == i:
                cnt += 1
            elif n % i == 0:
                cnt += 2
        if cnt > limit:
            div.append(power)
        else:
            div.append(cnt)
    return sum(div)


assert solution(5, 3, 2) == 10
assert solution(10, 3, 2) == 21

# Return the sum of available weapon stat(# of divisor) which does not exceed the limit, if it does,
# downgrade the stat as the power
