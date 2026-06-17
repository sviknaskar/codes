def kSum(arr, k, target):
    arr.sort()
    for i in range(len(arr)-k):
        sum = 0
        for j in range(k):
            sum += arr[i+j]
        # print(sum)
        if sum == target:
            return True
        if sum > target:
            break
    return False


def kSumTest():
    arr = [4,2,6,1,7,8]

    res = kSum(arr, 3, 17)
    print(res)

kSumTest()

