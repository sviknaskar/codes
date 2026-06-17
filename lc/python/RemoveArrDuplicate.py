def removeDuplicate(arr):
    arr.sort()
    print(arr)
    idx = 1
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            arr[idx] = arr[i+1]
            idx += 1

    print(arr)
    print(arr[:idx])


arr = [1,2,3,4,5,1,2,3,4,5,2]
removeDuplicate(arr)