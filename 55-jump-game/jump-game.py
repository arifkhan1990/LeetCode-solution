class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0

        for i in range(len(nums)):
            if reachable < i:
                return 0
            if reachable <= i+nums[i]:
                reachable = i+nums[i]
        return 1