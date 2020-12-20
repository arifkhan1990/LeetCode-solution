# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev, curr = None, head
        while curr:
            if val == curr.val:
                if prev is None:
                    if curr.next is not None:
                        head = curr.next
                    else:
                        head = None
                elif curr.next is None:
                    prev.next = None
                else:
                    prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head