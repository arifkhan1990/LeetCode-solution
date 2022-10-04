class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for w in words:
            is_not = 0
            for j in w:
                if j not in allowed:
                    is_not = 1
                    break
            if is_not == 1:
                ans += 1
        return len(words) - ans