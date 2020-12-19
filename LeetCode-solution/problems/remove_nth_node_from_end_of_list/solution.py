# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size, temp = 0, head
        while temp.next is not None:
            temp = temp.next
            size += 1
        size = size + 1 - n
        curr = prev = head
        if size == 0:
            if curr.next is not None:
                head = curr.next
            else:
                return None
        
        while size != 0:
            prev = curr
            curr = curr.next
            size -= 1
            
        if curr.next is None:
            prev.next = None
        else:
            prev.next = curr.next
        return head
            
                
        
        