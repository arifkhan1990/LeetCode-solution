class Solution:
    def uniqueLetterString(self, s):
        ch = [[] for _ in range(26)]
        for i in range(26):
            ch[i].append(-1)
        
        for i in range(len(s)):
            ch[ord(s[i]) - ord('A')].append(i)
        
        for i in range(26):
            ch[i].append(len(s))
        
        ans = 0
        for i in range(26):
            for j in range(1, len(ch[i])-1):
                l = ch[i][j] - ch[i][j-1] - 1
                r = ch[i][j+1] - ch[i][j] - 1

                ans += (l+1)*(r+1)
        return ans