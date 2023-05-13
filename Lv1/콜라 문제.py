def solution(a, b, n):
    ans = 0
    while n >= a:
        ans += (n // a) * b
        n = n % a + (n // a) * b
    return ans


# You can get 'b' bottles of new coke per 'a' bottles, if you give them to the market
# Return the total # of new cokes
