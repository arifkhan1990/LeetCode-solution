class Solution:
    def countSubstrings(self, s: str) -> int:
        ans, n = len(s), len(s)

        for i in range(n):
            for j in range(i+1, n):
                new_s = s[i:j+1]
                if new_s == new_s[::-1]:
                    ans += 1
        return ans
