def arrShiftK(arr, k):
    arr = arr[::-1]
    arr1 = arr[0:k][::-1]
    # arr1 = arr1[::-1]
    arr2 = arr[k:len(arr)][::-1]
    # arr2 = arr2[::-1]
    return arr1+arr2

def ArrShiftKTest():
    arr = [1,2,3,4,5,6,7,8,9]
    arr = arrShiftK(arr,3)
    print(arr)

ArrShiftKTest()