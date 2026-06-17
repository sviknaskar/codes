def threeSumTarget(arr, target = 0):
    arr.sort()

    res = []
    for i in range(len(arr)-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        left = i+1
        right = len(arr)-1
        while left<right:
            s = arr[i]+arr[left]+arr[right]
            print(s)
            if s == target:
                res.append([arr[i], arr[left], arr[right]])
                while left < right and arr[left] == arr[left+1]:
                    left += 1
                while left < right and arr[right] == arr[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
    return res

def threeSum(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates for left and right pointers
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


def ThreeSumTargetTest():
    arr = [4,5,2,-1,-3]
    r = threeSumTarget(arr)
    # r = threeSum(arr)
    print(r)

ThreeSumTargetTest()