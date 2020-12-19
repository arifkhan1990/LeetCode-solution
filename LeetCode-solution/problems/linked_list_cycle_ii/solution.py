# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        d = {}
        while fast:
            if fast in d.keys():
                return fast
            d[fast] = None
            fast = fast.next
        return None