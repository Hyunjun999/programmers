def solution(food):
    f = [1] + [food[i] // 2 for i in range(1, len(food))]
    res = "".join((map(lambda x: str(x) * f[x], range(1, len(f)))))
    res += "0" + res[::-1]
    return res

    # res = ''
    # for i in range(1, len(food)):
    #     if food[i] // 2 > 0:
    #         res += str(i) * (food[i] // 2)
    # res += '0'
    # res += ''.join(reversed(res[:-1]))
    # return res


# At this competition, two people will food-fight with given food-array. 0th index is always
# a cup of water that will determine who is the winner. In the array, each food
# will be divided equally to start from the leftmost and rightmost to reach the water in the middle
# For example, if the array is the [1, 7, 1, 2] the food will be distributed like '111303111'
# Return the food arrangment
