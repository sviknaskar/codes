def longestCommonSubStr(str1:str, str2:str):
    l1 = len(str1)
    l2 = len(str2)
    prev = [0]*(l1+1)

    res = 0
    for i in range(l2):
        curr = [0]*(l1+1)
        for j in range(l1):
            if str1[j] == str2[i]:
                curr[j+1] = prev[j]+1
                res = max(curr[j+1], res)
        print(curr)
        prev = curr


    print(res)


def LongestCommonSubStrTest():
    str1 = "abcd"
    str2 = "bcabc"
    longestCommonSubStr(str1, str2)


LongestCommonSubStrTest()