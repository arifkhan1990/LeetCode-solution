# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(for_head, s):
            s.append(for_head.val)
            if not for_head or not for_head.next:
                return for_head
           
            rev_h = reverse(for_head.next, s)
            for_head.next.next = for_head
            for_head.next = None

            return rev_h
        s = []
        rev_head = reverse(head, s)
        s1 = []
        while rev_head:
            s1.append(rev_head.val)
            rev_head = rev_head.next

        return s == s1
