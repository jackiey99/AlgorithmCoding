"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        stack = []
        dummy = head
        prev = dummy
        while dummy:
            if dummy.child:
                stack.append(dummy.next)
                dummy.next = dummy.child
                dummy.child.prev = dummy
                dummy.child = None
            prev = dummy
            dummy = dummy.next

        while stack:
            cur = stack.pop()
            while cur:
                prev.next = cur
                cur.prev = prev
                prev = prev.next
                cur = prev.next
        return head
