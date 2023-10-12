def solution(brown, yellow):
    answer = []
    elements = brown + yellow

    l = list(filter(lambda x: elements % x == 0, [i for i in range(1, elements + 1)]))

    if len(l) % 2 == 0:
        for i in range(0, len(l)):
            for j in range(len(l) - 1, 0, -1):
                if (
                    l[i] * l[j] == elements
                    and j >= i
                    and (l[i] - 2) * (l[j] - 2) == yellow
                ):
                    answer.append(l[j])
                    answer.append(l[i])
                continue
    else:
        answer.append(l[len(l) // 2])
        answer.append(l[len(l) // 2])
    return answer


# Carpet has two colors: brown and yellow, and its each edge should color with brown and
# yellow is inside of the brown tiles. Return the carpet's size based on the given number of tiles of brown and yellow.

assert solution(10, 2) == [4, 3]
assert solution(8, 1) == [3, 3]
assert solution(24, 24) == [8, 6]
