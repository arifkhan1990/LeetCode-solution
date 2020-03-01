class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        
class Solution:
    def addTwoNumbers(self, l1, l2):
        prev = result = ListNode(None)
        carray = 0
        
        while l1 or l2 or carray:
            if l1:
                carray += l1.val
                l1 = l1.next
            if l2:
                carray += l2.val
                l2 = l2.next
            
            prev.next = ListNode(carray % 10)
            prev = prev.next
            carray //= 10
        
        return result.next