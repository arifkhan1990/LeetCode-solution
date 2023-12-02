class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        ans = 0
        mxA = float('inf')
        while l < r:
            mxA = min(height[l], height[r]) * (r-l)
            ans = max(ans, mxA)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans