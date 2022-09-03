# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        p = q = head
        
        while q is not None and q.next is not None:
            p = p.next
            q = q.next.next
            if p == q:
                return True
        return False
        
            