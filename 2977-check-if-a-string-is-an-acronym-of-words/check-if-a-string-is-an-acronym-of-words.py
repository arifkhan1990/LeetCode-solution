class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        ans = ""
        for x in words:
            ans += x[0]
        return ans == s