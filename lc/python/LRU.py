from collections import deque


class cacheEntry:
    def __init__(self, v, k):
        self.key = k
        self.val = v

class lruc:
    def __init__(self, c = 5):
        self.cacheList = deque()
        self.cacheMap = {}
        self.capacity = c

    def get(self, k:int):
        if k not in self.cacheMap:
            return -1

        curr = k
        self.cacheList.remove(k)
        self.cacheList.appendleft(curr)
        self.cacheMap[k] = self.cacheMap[self.cacheList[0]]
        return self.cacheMap[k]




    def put(self, k:int, v:int):
        if k not in self.cacheMap:
            if len(self.cacheList) == self.capacity:
                #delete least recently used node from map and list
                curr = self.cacheList.pop()
                self.cacheMap.pop(curr)

            self.cacheList.appendleft(k)
            self.cacheMap[k] = v
        else:
            curr = k
            self.cacheList.remove(k)
            self.cacheList.appendleft(curr)
            self.cacheMap[k] = v



    def show(self):
        # for k,v in enumerate(self.cacheMap):
        #     print(f"key : {v.key} val: {v.val}")
        for i in self.cacheList:
            print(f"key:{i}    val: {self.cacheMap[i]}")



def lrucTest():
    cache = lruc()
    cache.put(1, 5)
    cache.put(2, 6)
    cache.put(3, 7)
    cache.show()
    print("get called 1")
    cache.get(1)
    cache.show()
    print("get called 2")
    cache.get(2)
    cache.show()
    print("put called")

    cache.put(3, 9)
    cache.put(3, 10)
    cache.put(3, 11)
    cache.show()

    print("put called")

    cache.put(4, 9)
    cache.put(5, 10)
    cache.put(6, 11)

    cache.show()
    print("invalid get called")
    cache.get(19)
    cache.show()
    print("valid get called")
    cache.get(2)
    cache.show()

lrucTest()