class Solution:
    def reverseWords(self, s: str) -> str:
        f = l = 0
        ansS = ''
        for i, c in enumerate(s):
            if i == len(s)-1:
                l += 1
            if c == ' ' or i == len(s)-1:
                while f < l:
                    ansS += s[l-1]
                    l -=1
                ansS += ' ' if i != len(s)-1 else ''
                f = l = len(ansS)
            else:
                l += 1
        return ansS