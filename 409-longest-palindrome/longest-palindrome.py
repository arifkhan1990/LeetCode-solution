class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        ans, hold = 0, 0
        for i,cnt in d.items(): 
            if cnt%2 == 1:
                ans += cnt - 1
                hold = 1
            else:
                ans += cnt 
        return ans+hold