def solution(x):
    string = str(x)
    num = 0
    for i in range(len(string)):
        num += int(string[i])
    return True if x % num == 0 else False

# return true if given x can be divided by sum of x's all digits

assert(solution(10) == True)
assert(solution(12) == True)
assert(solution(13) == False)
assert(solution(11) == False)