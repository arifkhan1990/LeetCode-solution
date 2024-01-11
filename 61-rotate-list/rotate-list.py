# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        curr = head

        len = 1
        while curr.next:
            curr = curr.next
            len += 1
        k %= len

        if k == 0:
            return head
        
        new_tail_p = len - k - 1
        new_tail = head

        for _ in range(new_tail_p):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        curr.next = head

        return new_head