class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        l = []
        i = 0

        while i < len(s):
            if s[i] == c:
                l.append(i)
            i += 1

        for i in range(len(s)):
            k = float('inf')
            for j in l:
                k = min(k, abs(i-j))
            ans.append(k)
        return ans