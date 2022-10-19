class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = Counter(nums)
        tp = n.most_common(1)
        return tp[0][0]