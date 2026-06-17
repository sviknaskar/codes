def MaxContainer(arr):
    left, right = 0, len(arr)-1
    maxArea = 0
    while left < right:
        tmpHeight = arr[left]
        if arr[right] < tmpHeight:
            tmpHeight = arr[right]
        diff = right - left
        area = tmpHeight * diff
        maxArea = max(area, maxArea)
        if arr[left]<arr[right]:
            left += 1
        else:
            right -= 1

    return maxArea


def MaxContainerTest():
    print(f"Test name: {__name__}")
    arr = [2, 1, 8, 6, 4, 6, 5, 5]
    res = MaxContainer(arr)
    print(res)