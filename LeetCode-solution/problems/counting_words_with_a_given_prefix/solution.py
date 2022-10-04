class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for x in words:
            if pref == x[:len(pref)]:
                ans += 1
        return ans