
def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1



def getLongestPalinSubStr(s:str):
    maxLen = 0
    startPos = -1
    for i in range(len(s)):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i+1)
        tmpLen = max(len1, len2)
        if tmpLen > maxLen:
            startPos = i - ( tmpLen + 1) //2
            maxLen = max(maxLen, tmpLen)

    return s[startPos+1: startPos+maxLen+1] , maxLen, startPos


def LongestPalinSubStrTest():
    print(f"Test name: {__name__}")
    str = "forgeeksskeegfor"
    subStr, l, _ = getLongestPalinSubStr(str)
    print(subStr)