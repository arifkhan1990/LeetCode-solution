# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def solve(head):
            if not head:
                return 0
            
            dv = head.val*2 + solve(head.next)
            head.val = dv % 10
            return dv // 10
        
        carry = solve(head)
        if carry:
            head = ListNode(carry, head)
        
        return head