# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def list_len(head):
            l = 0
            while head:
                l += 1
                head = head.next
            return l
        
        def reverse(head, k, l):
            if  l < k:
                return head
            
            cnt = 0
            prev, next_node, curr = None, None, head

            while cnt < k and curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                cnt += 1
            
            if next_node != None:
                head.next = reverse(next_node, k, l - k)
            
            return prev

        l = list_len(head)
        return reverse(head, k, l)
        