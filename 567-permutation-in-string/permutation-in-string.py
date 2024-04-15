class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)

        if l1 > l2:
            return 0
        
        cnt = Counter(s1)
        cur_wndw = Counter(s2[:l1])

        if cur_wndw == cnt:
            return 1
        
        for i in range(l1, l2):
            cur_wndw[s2[i]] += 1

            if cur_wndw[s2[i - l1]] == 1: 
                del cur_wndw[s2[i-l1]]
            else:
                cur_wndw[s2[i-l1]] -= 1
            
            if cur_wndw == cnt:
                return 1
        return 0
