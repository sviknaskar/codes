def removeElemFromArr(arr, elem):
    pos = 0
    for i in range(len(arr)):
        if arr[i] != elem:
            arr[pos] = arr[i]
            pos += 1

    while pos<len(arr):
        arr[pos] = -1
        pos+=1

def RemoveElemTest():
    arr = [1, 2, 1, 3, 5, 1, 1, 6]
    removeElemFromArr(arr, 1)
    print(arr)





RemoveElemTest()