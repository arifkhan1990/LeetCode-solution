class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)
        ans = []
        for i, d in x.most_common(k):
            ans.append(i)
        return ans