import itertools
def solution(num):
    # Using itertools to find the combination tuple whose sum is 0
    # l = list(itertools.combinations(num, 3))
    # tri = [sum(tup) for tup in l]
    # return tri.count(0)
    
    # Without itertools, how to find the relevant combinations..
    res = 0
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            for k in range(j + 1, len(num)):
                if num[i] + num[j] + num[k] == 0:
                    res += 1
    return res

assert(solution([-2, 3, 0, 2, -5]) == 2)
assert(solution([-3, -2, -1, 0, 1, 2, 3]) == 5)
assert(solution([[-1, 1, -1, 1]]) == 0)