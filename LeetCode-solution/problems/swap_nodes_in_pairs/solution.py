# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next 

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if head == None:
                return None
            if head.next == None:
                return head

            p , q = head, head.next
            if q:
                q = q.next
            p , p.next = p.next , p
            p.next.next = self.swapPairs(q)
            return p

        
        