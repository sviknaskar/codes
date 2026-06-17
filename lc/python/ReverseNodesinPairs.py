class node:
    def __init__(self, v):
        self.val = v
        self.next = None

def reverseNodesInPairs(head):
    dummy = node(0)
    # dummy.next = head
    tail, first = dummy, head
    while first and first.next:
        second = first.next
        first.next = second.next
        second.next = first
        tail.next = second
        tail = first
        first = first.next
    return dummy.next


def revLL(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev



h = node(1)
h.next = node(2)
h.next.next = node(3)
h.next.next.next = node (4)
h.next.next.next.next = node(5)

# r = reverseNodesInPairs(h)
r = revLL(h)
while r:
    print(r.val)
    r = r.next