class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        i, x = 0, Counter()
        while i < len(s):
            start = i
            x[ord(s[start])] = max(x[ord(s[start])], 1)
            j = start + 1
            while j < len(s) and (ord(s[j]) - ord(s[j-1]) == 1 or ord(s[j]) - ord(s[j-1]) == -25):
                j += 1
                x[ord(s[j - 1])] = max(x[ord(s[j-1])],  j - start)
            i = j
        return sum(x.values())