class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = 1

        while n in num_set:
            n += 1

        return n