class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        lidx = ridx = idx = -1

        for i, n in enumerate(nums):
            if not minK <= n <= maxK:
                idx = i
            
            if n == minK:
                lidx = i
            
            if n == maxK:
                ridx = i
            
            ans += max(0, min(lidx,ridx) - idx)
        return ans


