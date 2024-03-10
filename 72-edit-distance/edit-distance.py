class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def solve(w1, w2, i, j, dp):
            if i == len(w1):
                return len(w2) - j
            if j == len(w2):
                return len(w1) - i
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if w1[i] == w2[j]:
                return solve(w1, w2, i+1, j+1, dp)
            else:
                insert = 1 + solve(w1, w2, i, j+1, dp)
                delete = 1 + solve(w1, w2, i+1, j, dp)
                replace = 1 + solve(w1, w2, i+1, j+1, dp)
                ans = min(insert, delete, replace)
            
            dp[i][j] = ans
            return dp[i][j]
        
        dp = [[-1] * (len(word2)) for _ in range(len(word1))]
        return solve(word1, word2, 0, 0, dp)
