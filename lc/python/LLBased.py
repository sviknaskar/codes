class node:
    def __init__(self, val):
        self.val = val
        self.next = None


def showLL(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next


def midLL(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val


def revLL(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def revFromMid(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    curr, prev = slow, None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    showLL(head)
    showLL(prev)


def deleteNthNodeFromEnd(head, n):
    slow = fast = head
    while n:
        fast = fast.next
        n -= 1
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    showLL(head)




def LLTest():
    arr = [1,2,3,4,5,6,7,8,9]
    h = node(arr[0])
    curr = h
    for i in arr[1:]:
        tmp = node(i)
        curr.next = tmp
        curr = curr.next

    # showLL(h)
    # mid = midLL(h)
    # print(f"mid: {mid}")
    # print("reversed:")
    # r = revLL(h)
    # showLL(r)
    # revFromMid(h)
    showLL(h)
    print("after delete")
    deleteNthNodeFromEnd(h , 3)


LLTest()