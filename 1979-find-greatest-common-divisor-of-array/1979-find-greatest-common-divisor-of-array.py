class Solution:
    def gcd(self,n,m):
        if m == 0:
            return n
        else:
            return self.gcd(m, n%m)
    def findGCD(self, nums: List[int]) -> int:
        return self.gcd(max(nums), min(nums))