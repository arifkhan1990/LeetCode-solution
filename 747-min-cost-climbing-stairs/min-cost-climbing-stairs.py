class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n+1)

        def min_cost(cost, n):
            if dp[n] != -1:
                dp[n]
                return dp[n]
            
            if n <= 1:
                dp[n] = 0
            elif n == 2:
                dp[n] = min(cost[0], cost[1])
            else:
                dp[n] = min(min_cost(cost, n-1) + cost[n-1], min_cost(cost, n-2) + cost[n-2])
            return dp[n]
        return min_cost(cost, n)