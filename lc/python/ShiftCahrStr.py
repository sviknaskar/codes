def shiftCharByK(s, k):
    res = ""
    for i in range(len(s)):
        c = s[i]
        if c.isalpha():
            base = ord('a')
            if c.isupper():
                base = ord('A')
            newChar = chr((ord(c) + k - base)%26 + base)
            res += newChar
        else:
            res += c

    return res


def ShiftCharTest():

    s = "a2b1c"
    res = shiftCharByK(s,4)
    print(res)

ShiftCharTest()
