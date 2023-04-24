def solution(n, m):
    answer = []
    a = n
    b = m
    while True:
        if a > b:
            a = a % b
        else: b = b % a
        
        if a == 0:
            answer.append(b)
            break
        elif b == 0:
            answer.append(a)
            break
        elif a == 1 or b == 1:
            answer.append(1)
            break
    answer.append(int((n * m) / answer[0]))
    return answer

# Return LCM(Least Common Multiplier) and GCD(Greatest Common Divisior) in answer[0], answer[1] respectively
assert(solution(3, 12) == [3, 12])
assert(solution(2, 5) == [1, 10])