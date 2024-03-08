from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        cnt = list(freq.values())
        cnt.sort()
        ans = []
        for i in range(len(cnt) - 1, -1, -1):
            if len(ans) > 0 and cnt[i] != ans[-1]:
                break
            else:
                ans.append(cnt[i])
        return sum(ans)