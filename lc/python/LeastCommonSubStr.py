def leastCommonSubStr(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    maxLen = 0
    prev = [0]*(l1+1)
    for i in range(l2):
        curr = [0]*(l1+1)
        for j in range(l1):
            if s1[j] == s2[i]:
                curr[j+1] = prev[i]+1
                maxLen = maxLen(maxLen, curr[j+1])
    return maxLen