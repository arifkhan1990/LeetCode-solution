# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f, s = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return 1
        return 0