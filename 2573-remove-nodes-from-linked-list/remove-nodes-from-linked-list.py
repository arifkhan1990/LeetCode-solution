# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        st = []
        while cur:
            while st and st[-1].val < cur.val:
                st.pop()
            st.append(cur)
            cur = cur.next
        nxt = None
        while st:
            cur = st.pop()
            cur.next = nxt
            nxt = cur
        return cur