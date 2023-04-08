def solution(arr, divisor):
    l = list(filter(lambda x: x % divisor == 0, arr))
    l.sort()
    return l if len(l) >= 1 else [-1]

assert(solution([5, 9, 7, 10], 5) == [5, 10])
assert(solution([2, 36, 1, 3], 1) == [1, 2, 3, 36])
assert(solution([3,2,6], 10) == [-1])

#return ascending order array that contains the element of array 
# that can be divided by divisior else there is no element in return array,
# return [-1]