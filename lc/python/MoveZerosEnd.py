def moveZerosEnd(arr:list):
    pos = 0
    for i in range(len(arr)):
        if arr[i]:
            arr[pos] = arr[i]
            pos += 1
    for i in range(pos, len(arr)):
        arr[i] = 0



def moveZerosEndTest():
    arr = [0,0,0,1,2,0,3,4,0,5]
    print(arr)
    moveZerosEnd(arr)
    print(arr)
