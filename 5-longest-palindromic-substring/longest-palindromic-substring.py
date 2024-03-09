class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        st, ed = 0, 1

        # Initialize a table to store whether substrings are palindromes
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                st = i
                ed = 2

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > ed:
                        st = i
                        ed = length

        return s[st:st + ed]