class Solution:
    def countSubstrings(self, A: str) -> int:
        n = len(A)
        dp = [[0] * n for _ in range(n)]
        cnt = 0
        
        for i in range(n):
            dp[i][i] = 1
            cnt += 1
        for i in range(n-1):
            if A[i] == A[i+1]:
                dp[i][i+1] = 1
                cnt += 1
        
        for l in range(3, n+1):
            for s in range(n-l +1):
                e = s + l - 1
                if A[s] == A[e] and dp[s+1][e-1]:
                    dp[s][e] = 1
                    cnt += 1
        return cnt
