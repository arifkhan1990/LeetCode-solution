# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        even = None
        odd = head
        temp = None
        i = 1
        curr = ListNode()
        
        while odd is not None and odd.next:
            if i%2:
                if odd == head:
                    curr = odd
                    head = curr
                else:
                    curr.next = odd
                    curr = curr.next
            else:
                if i == 2:
                    even = odd
                    temp = even
                else:
                    even.next = odd
                    even = even.next
            i += 1
            odd = odd.next
            
        if odd is not None:
            if i%2:
                curr.next = odd
                curr = curr.next
                if even is not None:
                    even.next = None
            else:
                if even is not None:
                    even.next = odd
                    even = even.next
                    even.next = None
                else:
                    even = odd
                    even.next = None
                    temp = even

            if temp is not None:
                curr.next = temp
            else:
                curr.next = None
                
        return head

        