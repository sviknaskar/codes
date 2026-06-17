class Node:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None



def levelOrder(root):
    if root is None:
        return
    queue = [root]
    while queue:
        l = len(queue)
        level = []
        for i in range(l):
            curr = queue.pop(0)
            level.append(curr.val)

            if curr.left:
                queue.append(curr.left)

            if curr.right:
                queue.append(curr.right)
        print(level)



def dfs(root, target):
    stack = []
    curr = root
    res = []
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if curr.val == target:
            return True
        curr = curr.right
    return False

def preOrder(root, target):
    stack = [root]
    stackval = [root.val]
    tmp = []
    res = []
    sum = 0
    while stack:
        print(stackval, sum, tmp)
        curr = stack.pop()

        if curr.left == None and curr.right == None:
            sum -= curr.val
        else:
            sum += curr.val
        tmp.append(curr.val)
        stackval.pop()
        # print(curr.val)
        if curr.right:
            stack.append(curr.right)
            stackval.append(curr.right.val)
        if curr.left:
            stack.append(curr.left)
            stackval.append(curr.left.val)


    for e in res:
        print(e)



def PathSumTest():
    bst = Node(4)
    bst.left = Node(2)
    bst.left.left = Node(1)
    bst.left.right = Node(-1)

    bst.right = Node(-1)
    bst.right.left = Node(2)
    bst.right.right = Node(3)
    bst.right.right.right = Node(-1)

    levelOrder(bst)
    print("*"*30)
    # res = dfs(bst,4)
    # print(res)
    preOrder(bst,5)

PathSumTest()