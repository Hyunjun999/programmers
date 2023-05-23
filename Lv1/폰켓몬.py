def solution(nums):
    select = len(nums) // 2
    s = set(nums)
    return len(s) if len(s) <= select else select


assert solution([3, 1, 2, 3]) == 2
assert solution([3, 3, 3, 2, 2, 4]) == 3
assert solution([3, 3, 3, 2, 2, 2]) == 2
