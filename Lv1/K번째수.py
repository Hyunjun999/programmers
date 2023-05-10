def solution(array, commands):
    l = [sorted(array[c[0] - 1 : c[1]])[c[2] - 1] for c in commands]
    return l


# commands is a 2d-arr which contains the command whose length = 3 with elements: [start, end, pick]
# Based on the command, we have to slice the array from start idx to end idx and sort it and
# append the pick-th element in sorted sliced array to the result.

assert solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) == [5, 6, 3]
