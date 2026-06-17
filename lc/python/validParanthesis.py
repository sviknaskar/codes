def validBrackets(s:str):
    lookUp = {")":"(", "}":"{", "]":"["}
    stack = []
    for i in range(len(s)):
        if s[i] in lookUp:
            curr = stack.pop()
            if s[i] != curr and not stack:
                return False

        else:
            stack.append(s[i])

    return not stack