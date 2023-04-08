def solution(phone_number):
    last_index = len(phone_number) - 4
    return ''.join('*' * (last_index) + phone_number[last_index:])

assert(solution("01033334444") == "*******4444")
assert(solution("027778888") == "*****8888")

#return the phone number that covers with '*' except the last 4-digits.