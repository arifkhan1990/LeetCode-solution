class Solution:
    def replaceDigits(self, s: str) -> str:
        letter = "abcdefghijklmnopqrstuvwxyz";
        ansWord = ""
        for i,x in enumerate(s):
            if x.isnumeric():
                ansWord += letter[int(x) + (ord(s[i-1])-97)]
            else:
                ansWord += x
        return ansWord