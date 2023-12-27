class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        sm = 0
        mnL = float('inf')

        while r < len(nums):
            sm += nums[r]
            r += 1

            while sm >= target:
                mnL = min(mnL, r - l)
                sm -= nums[l]
                l += 1

        return mnL if mnL != float('inf') else 0