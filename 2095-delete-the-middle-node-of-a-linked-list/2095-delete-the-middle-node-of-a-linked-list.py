# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0, head)
        p = q = d
        while p.next and p.next.next:
            p = p.next.next
            q = q.next
        q.next = q.next.next
        return d.next