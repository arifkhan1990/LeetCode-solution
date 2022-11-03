class Solution:
    def repeatedCharacter(self, s: str) -> str:
        ans = ""
        mn = float('inf')
        for i in range(len(s)):
            k = s[i+1:].find(s[i]) + 1

            if k != 0:
                if mn > i+k:
                    ans = s[i]
                    mn = i+k
        return ans
                