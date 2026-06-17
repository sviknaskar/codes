def lenLongestSubStrUnique(s):
    l = {}
    left = 0
    maxLen = 0
    for right, char in enumerate(s):
        if char in l and left <= l[char]:
            left = l[char]+1
        l[char] = right
        maxLen = max(maxLen, right-left +1)
    return maxLen