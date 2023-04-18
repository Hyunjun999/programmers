def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            arr1[i][j] += arr2[i][j]
    return arr1

# Do matrix addition

assert(solution([[1,2],[2,3]], [[3,4],[5,6]]) == [[4,6],[7,9]])
assert(solution([[1],[2]], [[3],[4]]) == [[4],[6]])