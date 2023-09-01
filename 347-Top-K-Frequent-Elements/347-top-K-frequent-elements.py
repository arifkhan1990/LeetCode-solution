from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = [[] for i in range(len(nums) + 1)]
        count = Counter(nums)
  
        for n, c in count.items():
            ans[c].append(n)

        res = []
        for i in range(len(ans) - 1, 0, -1):
            for n in ans[i]:
                res.append(n)
                if len(res) == k:
                    return res