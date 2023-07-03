def solution(cards1, cards2, goal):
    res = []
    for w in goal:
        for w1 in cards1:
            if w1 == w:
                res.append(cards1.pop(0))
            break
        for w2 in cards2:
            if w2 == w:
                res.append(cards2.pop(0))
            break
    return "Yes" if res == goal else "No"


# Following the order in the cards1 and cards2, return yes if we can make goal or no
assert (
    solution(
        ["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]
    )
    == "Yes"
)

assert (
    solution(
        ["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]
    )
    == "No"
)
