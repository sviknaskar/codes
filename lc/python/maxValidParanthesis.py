def getMaxValidParanthesis(s):
    lt = {")":"(", "}":"{", "]":"["}
    stack = []
    maxLen = 0
    for c in s:
        if c in lt:
            if stack:
                top = stack.pop()
                if top == lt[c]:
                    maxLen += 1
        else:
            stack.append(c)

    return maxLen



def getMaxValidParenthesis2(s):
    open, close = 0, 0
    maxLen = 0
    for c in s:
        if c == "(":
            open += 1
        if c == ")":
            close += 1
        if close == open:
            maxLen = max(maxLen, 2*close)
        if close > open:
            close,open = 0,0

    open, close = 0, 0
    for i in range(len(s)-1, -1, -1):
        c = s[i]
        if c == "(":
            open += 1
        if c == ")":
            close += 1
        if close == open:
            maxLen = max(maxLen, 2*open)
        if open > close:
            close, open = 0, 0

    return maxLen


def maxValidParanthesisTest():
    s = "((()())))((()))"
    res = getMaxValidParanthesis(s)
    print(res)

    res = getMaxValidParenthesis2(s)
    print(res)

maxValidParanthesisTest()