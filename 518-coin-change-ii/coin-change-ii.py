class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def solve(idx, t):
            if idx == 0:
                return 0 if t%coins[0] != 0 else 1
            ntake = solve(idx-1, t)
            take = 0
            if coins[idx] <= t:
                take = solve(idx, t-coins[idx])

            return take + ntake
        return solve(len(coins)-1, amount)