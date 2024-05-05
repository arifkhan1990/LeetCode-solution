class Solution:
    def isValid(self, word: str) -> bool:
        v,c,l_ch,u_ch,d= 0, 0,0,0,0
        for i in word:
            if i.islower():
                l_ch = 1
                if i in "aeiou":
                    v = 1
                else:
                    c = 1
            elif i.isupper():
                u_ch = 1
                if i in "AEIOU":
                    v =  1
                else:
                    c = 1
            elif i.isdigit():
                d = 1
            elif not i.isdigit():
                return 0
        if len(word) > 2 and v and c and (d or l_ch or u_ch):
            return 1
        else:
            return 0