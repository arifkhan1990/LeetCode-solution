class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for x in words:
            i = 0
            j = len(x)-1
            is_palindrome = 1
            while i < j:
                if x[i] != x[j]:
                    is_palindrome = 0
                i , j = i+1, j-1
            if is_palindrome == 1:
                return x
        return ""
            