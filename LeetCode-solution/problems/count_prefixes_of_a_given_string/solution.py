class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for x in words:
            if x == s[:len(x)] and len(x) <= len(s):
                ans += 1
        return ans