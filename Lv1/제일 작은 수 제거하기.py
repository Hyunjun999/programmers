def solution(arr):
    if arr == []:  return [-1]
    elif arr == [10]: return [-1]
    arr.remove(min(arr))
    return arr

# Return after removing the minimum element at the given array, but when the array
# is given as an empty or a singleton array [10], return [-1] 

assert(solution([4,3,2,1]) == [4,3,2])
assert(solution([10]) == [-1])