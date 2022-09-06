class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low = low//2 
        high = (high+1)//2
        return high - low