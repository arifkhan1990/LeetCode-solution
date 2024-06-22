class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_L = 0
        count_R = 0
        balanced_count = 0
        
        for char in s:
            if char == 'L':
                count_L += 1
            elif char == 'R':
                count_R += 1
            
            if count_L == count_R:
                balanced_count += 1
                count_L = 0
                count_R = 0
                
        return balanced_count