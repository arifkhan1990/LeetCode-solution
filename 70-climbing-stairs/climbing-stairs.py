class Solution:
    def __init__(self):
        self.memo = {}

    def solve(self, n):
        if n == 0 or n == 1:
            return 1

        if n not in self.memo:
            l = self.solve(n-1)
            r = self.solve(n-2)
            self.memo[n] = l + r

        return self.memo[n]

    def climbStairs(self, n: int) -> int:
        return self.solve(n)