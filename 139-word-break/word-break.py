class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)

        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordset:
                    dp[i] = 1
                    break
        return dp[len(s)]
