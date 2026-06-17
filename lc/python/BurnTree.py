class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def levelOrder(root):
    if not root:
        return
    queue = [root]
    res = []
    while queue:
        l = len(queue)
        level = []
        for i in range(l):
            curr = queue[0]
            queue.pop(0)
            level.append(curr.val)
            # print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)


        res.append(level)

    for i in res:
        print(i)



def inorder(root):
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print(curr.val)
        curr = curr.right

def showInorderItr(root):
    stack = []
    curr = root
    while curr is not None or len(stack) != 0:
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        curr = stack[-1]
        print(curr.val)
        stack.pop()
        curr = curr.right

def BurnTest():
    tree = Node(10)

    tree.left = Node(5)
    tree.right = Node(15)

    tree.left.left = Node(3)
    tree.left.right = Node(7)
    tree.right.left = Node(13)
    tree.right.right = Node(17)

    tree.left.left.left = Node(1)
    tree.left.left.right = Node(4)
    tree.left.right.left = Node(6)
    tree.left.right.right = Node(8)
    tree.right.left.left = Node(10)
    tree.right.left.right = Node(15)
    tree.right.right.left = Node(16)
    tree.right.right.right = Node(20)


    levelOrder(tree)
    inorder(tree)

BurnTest()