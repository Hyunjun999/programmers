def solution(d, budget):
    d.sort()
    res = 0
    for e in d:
        budget -= e
        if budget < 0:
            break
        res += 1
    return res

# Reutrn the number of element that we can buy with the exactly given budget.
# In other words, we do not allow the more or less fee for the arbitrary element combination
# For example, [1,5,4,2] we cannot afford it since the sum is 12(exceeds the budget)

assert(solution([1,3,2,5,4], 9) == 3)
assert(solution([2,2,3,3], 10) == 4)