from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 > l2 :
            return 0

        
        cnt = Counter(s1)
        curr_window = Counter(s2[:l1])

        if curr_window  == cnt:
            return 1
        
        for i in range(l1, l2):
            curr_window[s2[i]] += 1

            if curr_window[s2[i - l1]] == 1:
                del curr_window[s2[i-l1]]
            else:
                curr_window[s2[i-l1]] -= 1
            
            if curr_window == cnt:
                return 1
        return 0