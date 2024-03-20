# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pre, curr, nxt = None, list1, list1
        ans = curr
        for _ in range(a):
            pre = curr
            curr = pre.next

        for _ in range(b+1):
            nxt = nxt.next
        pre.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = nxt
        return ans
            