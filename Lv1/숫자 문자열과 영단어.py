def solution(s):
    d = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for k in d.keys():
        if k in s:
            s = s.replace(k, str(d[k]))
    return int("".join(s))


# s is a string with combination of integer and string such as 'one4seveneight'
# we have to decode it to make the original integer.

assert solution("one4seveneight") == 1478
assert solution("23four5six7") == 234567
assert solution("2three45sixseven") == 234567
assert solution("123") == 123
