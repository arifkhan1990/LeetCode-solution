from collections import Counter
from heapq import heapify, heappop, heappush
from itertools import zip_longest

class Solution:
    def reorganizeString(self, s: str) -> str:
        ch_cnt = {}
        for ch in s:
            ch_cnt[ch] = ch_cnt.get(ch, 0) + 1
        
        max_heap = [(-cnt, ch) for ch , cnt in ch_cnt.items()]
        heapq.heapify(max_heap)

        res = []

        while len(max_heap) >= 2:
            cnt1, ch1 = heapq.heappop(max_heap)
            cnt2, ch2 = heapq.heappop(max_heap)

            res.extend([ch1, ch2])

            if cnt1 + 1 < 0:
                heapq.heappush(max_heap, (cnt1 + 1, ch1))
            if cnt2 + 1 < 0:
                heapq.heappush(max_heap, (cnt2 + 1, ch2))
        
        if max_heap:
            cnt, ch = heapq.heappop(max_heap)
            res.append(ch)

            if cnt + 1 < 0:
                return ""
        return "".join(res)
            


