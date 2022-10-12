class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ar = Counter(nums)
        top = ar.most_common(1)
        return top[0][0]