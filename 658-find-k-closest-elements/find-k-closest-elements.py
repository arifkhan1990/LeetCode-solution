import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for ele in arr:
            heapq.heappush(heap, (abs(x-ele), ele))
        
        ans = []
        while heap:
            dif, val = heapq.heappop(heap)
            ans.append(val)
            if len(ans) == k:
                break
        ans.sort()
        return ans
    