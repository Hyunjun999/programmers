def solution(numbers):
    return 45 - sum(numbers)

# Find the missing number in 'numbers' that contains elements 
# between 0 and 9 (there is no duplication among the elements)
# and return the sum of the missing number  

assert(solution([1,2,3,4,6,7,8,0]) == 14)
assert(solution([5,8,4,0,6,7,9]) == 6)