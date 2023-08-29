def solution(s):
    list = s.split()
    min = int(list[0])
    max = int(list[0])
    for i in range(len(list)):
        if int(list[i]) > max:
            max = int(list[i])
        if int(list[i]) < min:
            min = int(list[i])
    return str(min) + " " + str(max)


# 's' consists of integer with a single space btw numbers like '1 -4'
# Return a string with '(minimum) single-space (maximum)'
