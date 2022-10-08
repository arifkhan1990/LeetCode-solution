class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        n = gcd(a,b)
        
        ans = 0
        for i in range(1, int(sqrt(n))+1):
            if n%i == 0:
                if n//i == i:
                    ans += 1
                else:
                    ans += 2
        return ans