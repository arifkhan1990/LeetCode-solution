# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = ListNode()
        if l1 is None and l2 is None:
            return
        if l1 is None:
            head = l2
        elif l2 is None:
            head = l1
        else:
            i = 0
            while l1 or l2:
                if i == 0:
                    if l1.val < l2.val:
                        curr = l1
                        l1 = l1.next
                    else:
                        curr = l2
                        l2 = l2.next
                    head = curr
                if l2 is None:
                    curr.next = l1
                    l1 = l1.next
                elif l1 is None:
                    curr.next = l2
                    l2 = l2.next
                else:
                    if l1.val < l2.val:
                        curr.next = l1
                        l1 = l1.next
                    else:
                        curr.next = l2
                        l2 = l2.next
                curr = curr.next

                i = 1
        return head
        