# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, fst in enumerate(lists):
            if fst:
                heapq.heappush(heap, (fst.val, i, fst))
        
        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            curr.next = ListNode(val)
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i , node.next))

        return dummy.next