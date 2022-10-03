class Solution:
    def sortSentence(self, s: str) -> str:
        word = list(s.split(' '))
        
        ans = {}
        
        for i in word:
            id = i[-1:]
            ans[id] = i[:-1]
        
        res = []
        for i in sorted(ans):
            res.append(ans[i])
        return (' '.join(res))