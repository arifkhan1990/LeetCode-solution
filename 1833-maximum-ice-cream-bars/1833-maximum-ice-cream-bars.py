class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans, spend = 0, 0
        for i in costs:
            spend += i
            if spend <= coins:
                ans += 1
        return ans