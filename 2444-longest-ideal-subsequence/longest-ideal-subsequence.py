class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26

        for ch in s:
            curr = ord(ch) - ord('a')
            mx = 1
            for p in range(26):
                if abs(curr - p) <= k:
                    mx = max(mx, 1 + dp[p])
            dp[curr] = max(dp[curr], mx)
        return max(dp)