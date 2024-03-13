class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(i, j, dp):
            if i == len(text1):
                return 0
            if j == len(text2):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if text1[i] == text2[j]:
                dp[i][j] =  (1 + lcs(i+1, j+1, dp))
            else:
                dp[i][j] = max(lcs(i+1, j, dp), lcs(i, j+1, dp))
            return dp[i][j]
        dp = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        return lcs(0,0, dp)