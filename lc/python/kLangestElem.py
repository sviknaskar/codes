import heapq

def kLargest(arr,k):
    heap = []
    for i in arr:
        if len(heap) < k:
            heapq.heappush(heap, i)
        elif heap[0]<i:
            heapq.heappushpop(heap,i)
    return heap[0]


arr = [1,2,3,4,5,6,7,8,9]
print(kLargest(arr,6))