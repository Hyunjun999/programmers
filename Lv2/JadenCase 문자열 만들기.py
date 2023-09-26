def solution(s):
    l = s.split(" ")
    spaces = len(s.strip().split()) - 1
    l = [i.lower().capitalize() for i in l]
    res = ""
    for word in l:
        if word == "":
            res += " "
        else:
            res += word
            if spaces != 0:
                res += " "
                spaces -= 1
                continue
    return res


assert solution("3people unFollowed me") == "3people Unfollowed Me"
assert solution("for the last week") == "For The Last Week"

# Jaden Case is a convention that every word should start with uppercase and others should be lowercase
# But if the start letter is not alphabet, just convert remained letters as a lower
