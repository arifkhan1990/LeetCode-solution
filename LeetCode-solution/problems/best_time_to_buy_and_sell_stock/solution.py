class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s , b = 0, float('-inf')
        
        for i in prices:
            b = max( -i, b)
            s = max( i + b, s)
        return s
        