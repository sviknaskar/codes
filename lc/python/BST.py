import random

random.seed(13)

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
        q = []
        curr = self.root
        q.append(curr)
        while len(q) != 0:
            level = []
            l = len(q)
            for i in range(l):
                curr = q[0]
                q.pop(0)
                level.append(curr.val)
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)

            print(level)


    def preOrder(self):
        stack = [self.root]
        while stack:
            curr = stack.pop(0)
            print(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)




def BSTOrderTest():
    print(f"Test name: {__name__}")
    t = BST()
    for i in range(10):
        v = random.randint(0,30)
        print(v)
        t.insert(v)
    print("Inorder")
    t.showInorderItr()
    print("Level Order")
    t.levelOrder()
    print("Preorder ")
    t.preOrder()

def toLinearOrderItr(root:nodeBst):
    s = []
    dummy = nodeBst(-999)
    prev = dummy
    curr = root
    while s or curr:
        while curr:
            s.append(curr)
            curr = curr.left
        curr = s.pop()
        curr.left = None
        prev.right = curr
        prev = curr
        curr = curr.right

    return dummy.right



def toLinearOrder(root, tail = None):
    if root is None:
        return tail
    res = toLinearOrder(root.left, root)
    root.left = None
    root.right = toLinearOrder(root.right, tail)
    return res

def BSTLinearTest():
    print(f"Test name: {__name__}")
    t = BST()
    for i in range(10):
        v = random.randint(0, 30)
        print(v)
        t.insert(v)

    print("level order######")
    t.levelOrder()
    # r = toLinearOrder(t.root, None)
    r = toLinearOrderItr(t.root)
    print("Linear Tree###########")
    while r is not None:
        print(r.val)
        r = r.right


BSTOrderTest()