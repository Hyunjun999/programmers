def solution(n):
    list = [str(char) for char in str(n)]
    list.sort(reverse=True)
    return int(''.join((list)))

assert(solution(118372) == 873211)