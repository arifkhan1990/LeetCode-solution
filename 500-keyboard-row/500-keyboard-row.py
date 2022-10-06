class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        f = "qwertyuiop"
        s = "asdfghjkl"
        t = "zxcvbnm"
        ans = []
        for x in words:
            a=b=c= 0
            for i in x:
                if i in f:
                    a = 1
                if i in s:
                    b = 1
                if i in t:
                    c = 1
            if a+b+c == 1 :
                ans.append(x)
        return ans