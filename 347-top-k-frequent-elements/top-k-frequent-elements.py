import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        min_heap = [(-freq, item) for item, freq in cnt.items()]
        heapq.heapify(min_heap)

        ans = []
        for _ in range(k):
            freq, item = heapq.heappop(min_heap)
            ans.append(item)
        ans.sort()
        return ans
        