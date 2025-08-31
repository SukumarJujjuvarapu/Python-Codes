class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def createLinkedList():
    vals = list(map(int, input("Enter linked list elements separated by space: ").split()))
    dummy = ListNode()
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

head = createLinkedList()
reversed_head = reverseList(head)
print("Reversed Linked List:")
while reversed_head:
    print(reversed_head.val, end=" -> ")
    reversed_head = reversed_head.next
print("None")


##Given a singly linked list, reverse it in-place and return the new head.

