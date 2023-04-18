def solution(left, right):
    sign = lambda x: -1 if (x ** 0.5).is_integer() else 1
    return sum([sign(i) * i for i in range(left, right + 1)])

# Find the number of divisor from the left and right number inclusively.
# If the number of divisor each number is even, add all of them. 
# Else the number of divisor of each number is odd, subtract from the aggregate