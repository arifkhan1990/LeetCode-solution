# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = pre = ListNode(None)
        ans.next = head

        while head is not None:
            if head.val == val:
                pre.next, head.next, head = head.next, None, head.next
            else:
                pre, head = head, head.next
        return ans.next