def solution(str1, str2):
    l_a = [
        str1[i - 1 : i + 1].lower()
        for i in range(1, len(str1))
        if str1[i - 1].isalpha() and str1[i].isalpha()
    ]
    l_b = [
        str2[i - 1 : i + 1].lower()
        for i in range(1, len(str2))
        if str2[i - 1].isalpha() and str2[i].isalpha()
    ]

    inter, union = [], []
    d_a, d_b = {i: l_a.count(i) for i in l_a}, {i: l_b.count(i) for i in l_b}

    for e in d_a:
        if e in d_b:
            for _ in range(max(d_a[e], d_b[e])):
                union.append(e)
            for _ in range(min(d_a[e], d_b[e])):
                inter.append(e)

    for e in d_a:
        if e not in d_b:
            for _ in range(d_a[e]):
                union.append(e)
    for e in d_b:
        if e not in d_a:
            for _ in range(d_b[e]):
                union.append(e)

    if len(union) == 0:
        return 65536
    return int(len(inter) / len(union) * 65536)


assert solution("FRANCE", "french") == 16384
assert solution("handshake", "shake hands") == 65536
assert solution("aa1+aa2", "AAAA12") == 43690
assert solution("E=M*C^2", "e=m*c^2") == 65536
