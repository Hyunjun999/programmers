def solution(s):
    # return ''.join(sorted(list(s), reverse = True))
    return str("".join(reversed(sorted(s))))


# Sort the string 's' following the descending order.
# Assume that the uppercase is the smaller than the lowercase.

assert solution("Zbcdefg") == "gfedcbZ"
