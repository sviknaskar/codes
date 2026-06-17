class nodeList:
    def __init__(self, v):
        self.val = v
        self.next = None


class nodeBst:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

def sortedList2Bst(listHead):
    if not listHead:
        return listHead
    elif not listHead.next:
        return nodeBst(listHead.val)
    else:
        slow, fast = listHead, listHead
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next

        mid = pre.next
        pre.next = None
        root = nodeBst(mid.val)
        root.left = sortedList2Bst(listHead)
        root.right = sortedList2Bst(mid.next)
        return root


def bstPreOrder(root):
    if not root:
        return
    curr = root
    print(f"{root.val}")
    bstPreOrder(root.left)
    bstPreOrder(root.right)



def printList(head):
    curr = head
    while curr:
        print(f"curr val {curr.val} ->")
        curr = curr.next

def sortedList2BstTest():
    listHead = nodeList(1)
    listHead.next = nodeList(2)
    listHead.next.next = nodeList(3)
    listHead.next.next.next = nodeList(4)
    listHead.next.next.next.next = nodeList(5)
    listHead.next.next.next.next.next = nodeList(6)
    listHead.next.next.next.next.next.next = nodeList(7)
    # listHead.next.next.next.next.next.next.next = nodeList(8)
    # listHead.next.next.next.next.next.next.next.next = nodeList(9)
    # listHead.next.next.next.next.next.next.next.next.next = nodeList(10)
    printList(listHead)
    bstRoot = sortedList2Bst(listHead)
    bstPreOrder(bstRoot)

sortedList2BstTest()