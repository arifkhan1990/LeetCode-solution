class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count(strs):
            zero = one = 0
            for i in strs:
                if i == '0':
                    zero += 1
                elif i == '1':
                    one += 1
            return zero, one
        
        dp = [[0]*(n+1) for _ in range(m+1)]

        for s in strs:
            zero, one = count(s)
            for i in range(m, -1,-1):
                for j in range(n, -1, -1):
                    if i >= zero and j >= one:
                        dp[i][j] = max(dp[i][j], dp[i-zero][j-one] + 1)
        return dp[m][n]