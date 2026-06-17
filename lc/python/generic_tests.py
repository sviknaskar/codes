import heapq


class Node:
    def __init__(self, v = 0):
        self.val = v
        self.next = None



def lcss(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    prev = [0] * (l1+1)
    maxLen = 0
    for i in range(l2):
        curr = [0] * (l1+1)
        for j in range(l1):
            if s1[j] == s2[i]:
                curr[j+1] = prev[j]+1
                maxLen = max(maxLen, curr[j+1])
        prev = curr


def mergeKLists(lists):
    heap = []
    for l in lists:
        heapq.heappush(heap, (l.val , l))

    tmp = Node(-1)
    head = tmp
    while heap:
        curr = heapq.heappop(heap)[1]
        if curr:
            tmp.next = curr
            tmp = tmp.next
            if curr.next:
                heapq.heappush(heap, (curr.next.val, curr.next))

    return head.next


def MergeKListsTest():
    print(f"Test name: {__name__}")
    arr = []
    node1 = Node(1)
    node1.next = Node(3)
    node1.next.next = Node(5)
    node1.next.next.next = Node(7)
    arr.append(node1)

    node2 = Node(2)
    node2.next = Node(4)
    node2.next.next = Node(6)
    node2.next.next.next = Node(8)
    arr.append(node2)

    node3 = Node(0)
    node3.next = Node(9)
    node3.next.next = Node(10)
    node3.next.next.next = Node(11)
    arr.append(node3)

    mergedHead = mergeKLists(arr)
    while mergedHead:
        print(mergedHead.val)
        mergedHead = mergedHead.next


# MergeKListsTest()

def getLenUniqueSubStr(s:str):
    maxLen = 0
    left = 0
    lt = {}
    for right, char in enumerate(s):
        if char in lt and lt[char] >= left:
            left = lt[char] + 1
        lt[char] = right
        maxLen = max(maxLen, right-left+1)
    return maxLen


def revList(head):
    curr = head
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


def bstInorder(root):
    stack = []
    curr = root
    while curr is not None and stack:
        while curr is not None:
            stack.append(curr)
            curr = curr.next

        curr = stack.pop()
        print(curr.val)
        curr = curr.right


def preOrder(root):
    stack = [root]
    while stack:
        curr = stack.pop()
        print(curr)
        stack.append(curr.left)
        stack.append(curr.right)





def decodeString(s):
    currStr = ""
    currNum = 0
    lt = []
    decoded = ""
    for c in s:
        if c == "[":
            lt.append(currStr)
            lt.append(currNum)
            currStr = ""
            currNum = 0

        elif c == "]":
            num = lt.pop()
            prevStr = lt.pop()
            currStr = prevStr + num * currStr

        elif c.isnumeric():
            currNum = currNum * 10 + int(c)

        else:
            currStr += c

        print(lt)
        print(currStr)

    return currStr

# print(decodeString("3[c2[d]]"))


def longestValidParanthesis(s):
    stack = []
    lt = {")": "("}
    count = 0
    for c in s:
        if c == ")":
            if stack and stack.pop() == lt[c]:
                count += 1
        else:
            stack.append(c)

    return count

print(longestValidParanthesis("(()()(())))()"))



def rotateArray(arr, k):
    # print(arr)
    arr = arr[::-1]
    # print(arr)
    arrL = arr[:k][::-1]
    # print(arrL)
    arrR = arr[k:][::-1]
    # print(arrR)
    arr = arrL+arrR
    # print(arr)
    return arr


def searchInRotatedArray(arr, target):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target and target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target and target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# rotatedArr = rotateArray([1,2,3,4,5,6,7,8,9] , 3)
# print(rotatedArr)
# x = searchInRotatedArray(rotatedArr, 6)
# print(x)


class interval:
    def __init__(self, s = -1, e = -1):
        self.start = s
        self.end = e

def mergeIntervals(intervals):
    intervals.sort(key = lambda x:x.start)
    lt = [intervals[0]]
    for i in intervals[1:]:
        prev = lt[-1]
        if i.start <= prev.end:
            prev.end = max(i.end, prev.end)
        else:
            lt.append(i)

    return lt


def insertIntervals(intervals, newInterval):
    mergedInterval = mergeIntervals(intervals)
    count = 0
    res = []
    while count < len(mergedInterval) and mergedInterval[count].end < newInterval.start:
        res.append(mergedInterval[count])
        count += 1

    while count < len(mergedInterval) and mergedInterval[count].start < newInterval.end:
        newInterval.start = min(newInterval.start, mergedInterval[count].start)
        newInterval.end = max(newInterval.end, mergedInterval[count].end)
        count += 1

    res.append(newInterval)
    for i in range(count, len(mergedInterval)):
        res.append(mergedInterval[i])

    return res


# intervals = [interval(2,5), interval(1,3), interval(7,8), interval(6,8), interval(12,15)]
# # res = mergeIntervals(intervals)
# res = insertIntervals(intervals, interval(7,13))
# for i in res:
#     print(f"[{i.start}, {i.end}]")

def findIslands(mat):
    rows = len(mat)
    cols = len(mat[0])
    def dfs(r,c, area = 0):
        if r < 0 or r >= rows or c < 0 or c >= cols or mat[r][c] == 0:
            return
        mat[r][c] = 0
        dfs(r-1, c, area)
        dfs(r+1, c, area)
        dfs(r, c-1, area)
        dfs(r, c+1, area)
        return area


    count = 0
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                count += 1
                area = dfs(i,j)
                for ii in range(rows):
                    print(mat[ii])
                print(f"area : {area}")
                print("*"*30)


    return count

# mat = [
#     [0,1,0,1],
#     [1,0,0,0],
#     [0,0,1,1],
#     [1,1,1,0]
# ]
#
# res = findIslands(mat)
# print(mat)
# print(res)

def threeSumTarget(arr, target = 0):
    arr.sort()
    res = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        left = i+1
        right = len(arr)-1
        while left < right :
            tot = arr[i]+arr[left]+arr[right]
            if tot == target:
                res.append([arr[i], arr[left], arr[right]])
                left +=1
                right -=1
            elif tot<0:
                left += 1
            else:
                right -= 1
    return res
#
# r = threeSumTarget([-1,0,1,2,-1,-1])
# print(r)


def transpose(mat):
    rows = len(mat)
    cols = len(mat[0])
    matT = [[0 for _ in range(rows)] for _ in range(cols)]

    for r in range(rows):
        for c in range(cols):
            matT[c][r] = mat[r][c]

    # for i in range(cols):
    #     print(matT[i])
    return matT


def rotateImage(mat):
    matT = transpose(mat)
    for i in range(len(matT)):
        matT[i] = matT[i][::-1]
    for i in range(len(matT)):
        print(matT[i])


mat = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

rotateImage(mat)












