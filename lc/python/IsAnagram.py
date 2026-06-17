def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False

    lt1, lt2 = {}, {}
    for c in s1:
        if c in lt1:
            lt1[c] += 1
        else:
            lt1[c] = 1
        if c in s2:
            if c in lt2:
                lt2[c] += 1
            else:
                lt2[c] = 1
        else:
            return False

    return lt1 == lt2


def AnagramTest():
    s1 = "silent"
    s2 = "listen"

    print(isAnagram(s1, s2))

AnagramTest()
