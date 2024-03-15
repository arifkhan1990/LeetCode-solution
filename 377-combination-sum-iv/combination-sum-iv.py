class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def solve(n, t):
            if t < 0:
                return 0
            
            if t == 0:
                return 1
            ans = 0
            for i in range(n):
                ans += solve(n, t - nums[i])
            return ans
        return solve(len(nums), target)