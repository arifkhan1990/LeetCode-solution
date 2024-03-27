class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        pre_cnt1 = Counter(word1)
        pre_cnt2 = Counter(word2)

        # Check if the sets of characters are equal
        if set(pre_cnt1.keys()) != set(pre_cnt2.keys()):
            return False
        
        # Check if the sets of counts are equal
        if set(pre_cnt1.values()) != set(pre_cnt2.values()):
            return False
        
        return sorted(pre_cnt1.values()) == sorted(pre_cnt2.values())