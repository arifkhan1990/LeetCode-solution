class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        if n <= 2:
            return False
    
        for base in range(2, n - 1):
            num_str = ''
            num = n
            while num > 0:
                num_str = str(num % base) + num_str
                num //= base
            
            if num_str != num_str[::-1]:
                return False
        
        return True