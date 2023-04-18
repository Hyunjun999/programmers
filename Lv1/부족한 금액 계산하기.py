def solution(price, money, count):
    total = 0
    while count != 0:
        total += price * count
        count -= 1
    if money >= total:
        return 0
    else:
        return total - money

# Initial price will be multiplied by from 1 to 'count' finally
# Thus, return the deficient money from the total money.

assert(solution(3, 20, 4) == 10)