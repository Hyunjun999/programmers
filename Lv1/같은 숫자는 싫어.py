def solution(arr):
    answer = [arr[0]]
    for e in arr:
        if answer[-1] != e:
            answer.append(e)
    return answer

# Return the array that does not allow the consecutive numbers. For example,
# if arr = [1, 1, 3, 3, 0, 1, 1], return [1, 3, 0, 1]

assert(solution([1, 1, 3, 3, 0, 1, 1]) == [1, 3, 0, 1])
assert(solution([4,4,4,3,3]) == [4, 3])