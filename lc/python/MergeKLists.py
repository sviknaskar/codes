import heapq
import LCSol.LL as ll


def mergeKLists(lists):
    heap = []
    for node in lists:
        if node:
            heapq.heappush(heap, (node.val, node))

    tmp = ll.Node(-1)
    head = tmp
    while heap:
        smallestNode = heapq.heappop(heap)[1]
        tmp.next = smallestNode
        tmp = tmp.next
        if smallestNode.next:
            heapq.heappush(heap, (smallestNode.next.val, smallestNode.next))

    return head


def MergeKListsTest():
    print(f"Test name: {__name__}")
    arr = []
    node1 = ll.Node(1)
    node1.next = ll.Node(3)
    node1.next.next = ll.Node(5)
    node1.next.next.next = ll.Node(7)
    arr.append(node1)

    node2 = ll.Node(2)
    node2.next = ll.Node(4)
    node2.next.next = ll.Node(6)
    node2.next.next.next = ll.Node(8)
    arr.append(node2)

    node3 = ll.Node(0)
    node3.next = ll.Node(9)
    node3.next.next = ll.Node(10)
    node3.next.next.next = ll.Node(11)
    arr.append(node3)

    mergedHead = mergeKLists(arr)
    while mergedHead:
        print(mergedHead.val)
        mergedHead = mergedHead.next