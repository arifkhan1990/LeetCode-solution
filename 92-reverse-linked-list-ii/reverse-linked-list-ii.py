# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head and left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        for _ in range(left-1):
            pre = pre.next
        
        curr, n_node = pre.next, None

        for _ in range(right - left + 1):
            tmp = curr.next
            curr.next = n_node
            n_node = curr
            curr = tmp
        
        pre.next.next = curr
        pre.next = n_node

        return dummy.next