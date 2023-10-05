def solution(s):
    bi = ""
    answer = [0, 0]
    l = list(filter(lambda x: x == "1", s))
    answer[0] += 1
    dec = len(l)
    num_of_zero = len(s) - len(l)
    answer[1] += num_of_zero
    bi = bin(dec).replace("0b", "")
    if bi == "1":
        return answer

    while bi != "1":
        rec = list(filter(lambda x: x == "1", bi))
        answer[0] += 1
        dec = len(rec)
        num_of_zero = len(bi) - len(rec)
        answer[1] += num_of_zero
        bi = bin(dec).replace("0b", "")
    return answer


# s is a string that consists of 0 and 1. Before binary convert, remove all zeros and
# try to change the length of removed zero string into binary number. Return the array
# contatins the number of binary change and number of zeros that you have removed
assert solution(
    "110010101001",
) == [3, 8]

assert solution("01110") == [3, 3]
assert solution("1111111") == [4, 1]
