class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        pre_cnt1 = list(Counter(word1).values())
        pre_cnt2 = list(Counter(word2).values())
        
        return (sorted(word1) == sorted(word2) or sorted(pre_cnt1) == sorted(pre_cnt2)) and set(word1) == set(word2)