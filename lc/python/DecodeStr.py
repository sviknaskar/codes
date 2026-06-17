def decodeStr(s):
    stack = []
    currStr = ""
    currNum = 0
    for c in s:
        if c == "[":
            stack.append(currStr)
            stack.append(currNum)
            currStr = ""
            currNum = 0
        elif c == "]":
            num = stack.pop()
            prevStr = stack.pop()
            currStr =  prevStr + currStr * num

        elif c.isnumeric():
            currNum = currNum*10+int(c)
        else:
            currStr += c

        print(stack)
    return currStr


def DecodeStrTest():
    s = "3[a3[c]]"
    decoded = decodeStr(s)
    print(decoded)

DecodeStrTest()