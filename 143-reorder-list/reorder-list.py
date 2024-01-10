# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(right):
            prev, curr = None, right

            while curr is not None:
                n_node = curr.next
                curr.next = prev
                prev = curr
                curr = n_node
            return prev
        
        def merge_list(list1, list2):
            while list2:
                next_list1, next_list2 = list1.next, list2.next
                list1.next, list2.next = list2, next_list1
                list1, list2 = next_list1, next_list2

        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right = slow.next
        slow.next= None

        right = reverse(right)

        merge_list(head, right)



