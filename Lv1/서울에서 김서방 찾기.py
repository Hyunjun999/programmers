def solution(seoul):
    return '김서방은 ' + str(list(map(lambda x: x == 'Kim', seoul)).index(True)) +'에 있다'

assert(solution(["Jane", "Kim"]) == "김서방은 1에 있다")