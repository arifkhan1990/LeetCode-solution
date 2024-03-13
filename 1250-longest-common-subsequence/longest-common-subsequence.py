class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def lcs(i, j):
            if i == len(text1):
                return 0
            if j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return (1 + lcs(i+1, j+1))
            else:
                return max(lcs(i+1, j), lcs(i, j+1))
        return lcs(0,0)