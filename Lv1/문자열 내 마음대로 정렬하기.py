def solution(strings, n):
    # strings.sort()
    # strings.sort(key=lambda x: x[n])
    # return strings
    return sorted(sorted(strings), key=lambda x: x[n])


# Based on the n-th character, sort the str in the strings list. If there are same characters at that index,
# then sort with the lexicographical order

assert solution(["sun", "bed", "car"], 1) == ["car", "bed", "sun"]
assert solution(["abce", "abcd", "cdx"], 2) == ["abcd", "abce", "cdx"]
assert solution(["aea", "ba", "ce", "aee"], 1) == ["ba", "aea", "aee", "ce"]
