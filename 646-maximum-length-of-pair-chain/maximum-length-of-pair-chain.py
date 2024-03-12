class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[0])
        n = len(pairs)
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1] and dp[i] < dp[j]+1:
                    dp[i] = 1 + dp[j]
        return max(dp)
