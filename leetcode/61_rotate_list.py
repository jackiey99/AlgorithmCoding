# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None:
            return head

        tail, size = head, 1
        while tail.next:
            tail = tail.next
            size += 1

        k = k % size
        if k == 0:
            return head

        p = head
        for _ in range(size - k - 1):
            p = p.next

        new_head = p.next
        tail.next = head
        p.next = None

        return new_head
