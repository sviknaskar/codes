class Node:
    def __init__(self, v):
        self.val = v
        self.next = None


def removeDuplicates(head):
    tmp = Node(0)
    newHead = tmp
    curr = head
    while curr and curr.next:
        while curr and curr.val == curr.next.val:
            curr = curr.next
        tmp.next = curr.next
        tmp = tmp.next
        curr = curr.next
    head = newHead.next

def printList(head):
    curr = head
    while curr:
        print(f"curr val {curr.val} ->")
        curr = curr.next

def RemoveListDuplicatesTest():
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(2)
    head.next.next.next.next.next.next = Node(3)
    printList(head)
    print("#"*30)
    # newHead = removeDuplicates(head)
    removeDuplicates(head)
    printList(head)

RemoveListDuplicatesTest()
