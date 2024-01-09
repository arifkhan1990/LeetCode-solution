# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(left, right):
            if not left:
                return right
            if not right:
                return left
            
            result = None

            if left.val <= right.val:
                result = left
                result.next = merge(left.next, right)
            else:
                result = right
                result.next = merge(left, right.next)
            return result

        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right = slow.next
        slow.next = None

        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right)

        return merge(left_sorted, right_sorted)