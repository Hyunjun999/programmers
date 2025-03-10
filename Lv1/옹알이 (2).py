# 머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 조합해서 만들 수 있는 발음밖에 하지 못하고
# 연속해서 같은 발음을 하는 것을 어려워합니다. 문자열 배열 babbling이 매개변수로 주어질 때,
# 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.


def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for b in babbling:
        prev = ""
        while True:
            if b[:3] in can:
                if b[:3] == prev:
                    break
                prev = b[:3]
                b = b[3:]
            elif b[:2] in can:
                print(b[:2])
                if b[:2] == prev:
                    break
                prev = b[:2]
                b = b[2:]
            else:
                break

        if not b:
            cnt += 1

    return cnt


assert solution(["aya", "yee", "u", "maa"]) == 1
assert solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]) == 2
