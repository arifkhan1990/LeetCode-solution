class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(s):
            i, j = 0, len(s)-1
            while i < j:
                if s[i] != s[j]:
                    return 0
                i += 1
                j -= 1
            return 1

        i, j, k  = 0, len(s)-1, 0
        while i < j:
            if s[i] != s[j]:
                x = s[i+1:j+1]
                if is_palindrome(x) == 0:
                    k += 1
                else:
                    i += 1
                x = s[i:j]
                if is_palindrome(x) == 0:
                    k += 1
                else:
                    j -= 1
            else:
                i += 1
                j -= 1
            if k > 1:
                return 0
        return k <= 1
                