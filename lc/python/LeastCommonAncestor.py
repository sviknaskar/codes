import collections
import random

random.seed(42)

class nodeBst:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, v):
        tmpNode = nodeBst(v)
        if self.root == None:
            self.root = tmpNode
        else:
            curr = self.root
            while True:
                if curr.val >= v:
                    if curr.left is None:
                        curr.left = tmpNode
                        break
                    else:
                        curr = curr.left

                else:
                    if curr.right is None:
                        curr.right = tmpNode
                        break
                    else:
                        curr = curr.right


    def showInorderItr(self):
        stack = []
        curr = self.root
        while curr is not None or len(stack) != 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack[-1]
            print(curr.val)
            stack.pop()
            curr = curr.right

    def levelOrder(self):
        q = collections.deque()
        curr = self.root
        q.append(curr)
        while len(q):
            s = len(q)
            level = []
            for i in range(s):
                v = q[0]
                level.append(v.val)
                q.popleft()
                if v.left:
                    q.append(v.left)
                if v.right:
                    q.append(v.right)
            print(level)

    def getLCA(self, v1, v2):
        curr = self.root
        while curr:
            if curr.val > v1 and curr.val > v2:
                curr = curr.left
            elif curr.val < v1 and curr.val < v2:
                curr = curr.right
            else:
                return curr





def LCATest():
    # l = [4,2,1,3,6,5,7]
    l = []
    for i in range(10):
        n = random.randint(1,100)
        print(n)
        l.append(n)
    print("#"*40)
    t = BST()
    for i in l:
        t.insert(i)
    t.showInorderItr()
    # lca = t.getLCA()
    print("#" * 40)
    t.levelOrder()
    print("#" * 40)
    lca = t.getLCA(14,18)
    print(f"lca : {lca.val}")

LCATest()
