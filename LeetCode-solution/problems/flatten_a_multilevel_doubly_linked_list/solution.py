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
        s = []
        curr = head

        while head:
            if head.child:
                if head.next:
                    s.append(head.next)
                head.next = head.child
                head.next.prev = head
                head.child = None
            elif not head.next and s:
                head.next = s.pop()
                head.next.prev = head
            head = head.next

        return curr