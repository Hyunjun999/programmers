def solution(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])

# Do the dot product with two arry 'a' and 'b'

assert(solution([1,2,3,4], [-3,-1,0,2]) == 3)
assert(solution([-1,0,1], [1,0,-1]) == -2)