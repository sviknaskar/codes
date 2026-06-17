class Node:
    def __init__(self, v):
        self.val = v
        self.next = None
        self. random = None


def printList(head):
    curr = head
    while curr:
        print(f"curr val {curr.val}")
        if curr.random:
            print(f"curr random ptr val: {curr.random.val}")
        else:
            print(f"no random pointer")
        curr = curr.next


def cloneLL(head):
    curr = head
    while curr is not None:
        tmpNode = Node(curr.val)
        tmpNode.next = curr.next
        curr.next = tmpNode
        curr = tmpNode.next

    curr = head
    while curr is not None:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    # printList(head)

    curr = head
    cloneHead = head.next
    clone = cloneHead
    while clone.next is not None:
        curr.next = curr.next.next
        clone.next = clone.next.next
        curr = curr.next
        clone = clone.next
    curr.next = None
    clone.next = None
    printList(cloneHead)

def LLWithRandomPtrTest():
    # Creating a linked list with random pointer
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next.next
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head.next

    # Print the original list
    # print("Original linked list:")
    # printList(head)

    # clonedList = cloneLinkedList(head)
    #
    # print("Cloned linked list:")
    # printList(clonedList)
    cloneLL(head)

LLWithRandomPtrTest()