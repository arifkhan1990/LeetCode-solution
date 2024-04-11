class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        mx, mn = 0, float('-inf')
        while i < len(prices):
            mn = max(-prices[i], mn)
            mx = max(prices[i]+mn, mx)
            i += 1
        return mx