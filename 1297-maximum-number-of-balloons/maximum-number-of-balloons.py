class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash = {'b':0,'a':0,'l':0,'o':0,'n':0}
        for i in text:
            if i in "balon":
                hash[i] += 1
        ans = min(hash['b'],hash['a'],hash['l']//2, hash['o']//2,hash['n'])
        return ans