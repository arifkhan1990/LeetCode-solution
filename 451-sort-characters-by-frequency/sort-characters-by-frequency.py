from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        ans = cnt.most_common()
        res = ""
        for x in ans:
            res += x[0]*x[1]
        return res