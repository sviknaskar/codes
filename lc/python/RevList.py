import LCSol.LL as ll
def rotateList(headNode):
    prev = None
    curr = headNode
    next = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


def RevListTest():
    print(f"Test name: {__name__}")
    node1 = ll.Node(1)
    node1.next = ll.Node(3)
    node1.next.next = ll.Node(5)
    node1.next.next.next = ll.Node(7)

    curr = node1

    while curr:
        print(curr.val)
        curr = curr.next

    newHead = rotateList(node1)
    curr = newHead

    while curr:
        print(curr.val)
        curr = curr.next
