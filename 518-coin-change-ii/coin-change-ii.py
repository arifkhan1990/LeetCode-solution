class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def solve(idx, t, dp):
            if idx == 0:
                if t%coins[0] != 0:
                    dp[idx][t] = 0
                else:
                    dp[idx][t] = 1
                return dp[idx][t]
            if dp[idx][t] != -1:
                return dp[idx][t]
            ntake = solve(idx-1, t, dp)
            take = 0
            if coins[idx] <= t:
                take = solve(idx, t-coins[idx], dp)
            dp[idx][t] = take+ntake
            return dp[idx][t]

        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n+1)]
        return solve(n-1, amount, dp)