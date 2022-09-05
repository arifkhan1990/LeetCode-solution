# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = ListNode(0)
        tmp.next = head
        p , q = tmp, head
        
        while n > 0:
            q = q.next
            n -= 1
            
        while q:
            p, q = p.next, q.next
            
        p.next = p.next.next
        
        return tmp.next