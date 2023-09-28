def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer


# Choose one number from the arrays A and B and multiply it by two numbers.
# Repeat this process by the length of the array, accumulating the values multiplied by the two numbers and adding them.
# The goal is to make the final accumulated value minimal.

assert solution([1, 4, 2], [5, 4, 4]) == 29
assert solution([1, 2], [3, 4]) == 10
