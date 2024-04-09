class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return 0
        ans = float('inf')
        nums.sort()
        l, r = 0, k-1

        while r < n:
            curr = nums[r] - nums[l]
            ans = min(ans, curr)
            l += 1
            r += 1
        return ans