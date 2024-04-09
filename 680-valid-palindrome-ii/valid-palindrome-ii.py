class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j  = 0, len(s)-1
        while i < j:
            if s[i] != s[j]:
                x1 = s[i+1:j+1]
                x2 = s[i:j]
                return x1 == x1[::-1] or x2 == x2[::-1]
            i += 1
            j -= 1

        return 1
                