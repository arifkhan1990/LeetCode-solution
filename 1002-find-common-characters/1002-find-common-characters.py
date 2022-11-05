class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        res = Counter(words[0])
        for x in words:
            res &= Counter(x)
            
        for i in res:
            k = [i]*res[i]
            ans += k
        return ans
        