from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1 = Counter(words1)
        w2 = Counter(words2)
        
        ans = 0
        for i in words1:
            if w1[i] == 1 and w2[i] == 1:
                ans += 1
        return ans