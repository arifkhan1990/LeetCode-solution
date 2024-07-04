# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        md = head.next
        nxs = md

        while nxs:
            t = 0

            while nxs.val != 0:
                t += nxs.val
                nxs = nxs.next
            
            md.val = t
            nxs = nxs.next

            md.next = nxs
            md = md.next
        return head.next