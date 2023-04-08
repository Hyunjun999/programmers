def solution(absolutes, signs):
    l = [pair for pair in zip(absolutes, signs)]
    res = []
    for i in l :
        res.append(-i[0]) if i[1] == False else res.append(i[0])
    return sum(res)

assert(solution([4,7,12], [True, False, True]) == 9)
assert(solution([1,2,3], [False,False,True]) == 0)

#Based on the signs, we have to make a new array after we 
# give sign to the element of absolutes. Then return
# the summation of the that new array.