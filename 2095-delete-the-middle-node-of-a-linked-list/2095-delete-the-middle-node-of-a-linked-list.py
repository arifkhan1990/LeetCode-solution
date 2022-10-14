# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = r = head
        i = 0
        while p:
            p = p.next
            i += 1
        if i == 1:
            r = head = None
            return head
        i //= 2
        while i > 1:
            r = r.next
            i -= 1
        r.next = r.next.next
        return head