import heapq
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        heap = [(-fre, ch) for ch, fre in cnt.items()]
        heapq.heapify(heap)

        res = ""
        while heap:
            fre, ch = heapq.heappop(heap)
            res += ch*(-fre)
        return res