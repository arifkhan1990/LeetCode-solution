class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, sm = 0, 0, 0
        mnl = float("inf")

        while r < len(nums):
            sm += nums[r]
            r += 1

            while sm >= target:
                mnl = min(mnl, r - l)
                sm -= nums[l]
                l += 1
        return mnl if mnl != float('inf') else 0