# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = dum = ListNode(None)

        while list1 is not None or list2 is not None:
            if list1 is not None and list2 is not None and list1.val <= list2.val:
                ans.next = list1
                list1 = list1.next
            elif list1 is not None and list2 is not None and list1.val > list2.val:
                ans.next = list2
                list2 = list2.next
            elif list1 is None:
                ans.next = list2
                list2 = list2.next
            else:
                ans.next = list1
                list1 = list1.next
            ans = ans.next
        return dum.next
                
                