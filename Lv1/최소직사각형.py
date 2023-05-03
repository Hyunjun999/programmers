def solution(sizes):
    w, h = [], []
    for s in sizes:
        w.append(max(s))
        h.append(min(s))
    return max(w) * max(h)

# Return the smallest area of the business card wallet that can contain all cards.
# But, you can change the width and height length to decrease the area of the wallet