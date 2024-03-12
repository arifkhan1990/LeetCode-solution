# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = 0
        d = ListNode(0)
        d.next = head
        s = {0: d}

        node = head
        while node:
            pre += node.val
            s[pre] = node
            node = node.next
        
        pre = 0
        node = d
        while node:
            pre += node.val
            node.next = s[pre].next
            node = node.next
        return d.next