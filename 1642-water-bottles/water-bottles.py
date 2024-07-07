class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty = numBottles
        extra = 0
        while empty >= numExchange:
            ans = ans + empty//numExchange
            extra = empty%numExchange
            empty = (empty // numExchange) + extra 
        return ans