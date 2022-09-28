class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pS = 1
        dS = 0
        
        while n  > 0:
            pS *= n%10
            dS += n%10
            n //= 10
            
        
        return pS - dS