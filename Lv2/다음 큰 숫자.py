def solution(n):
    temp = n + 1
    while bin(temp).replace("0b", "").count("1") != bin(n).replace("0b", "").count("1"):
        temp += 1
    return temp


# Return the number that greater than n which satisfies the number of 1, when we convert
# both n and the number greater than n into binary, the number of 1 is same.
