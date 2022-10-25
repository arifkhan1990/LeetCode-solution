class Solution:
    def gcd(self,n,m):
        if m == 0:
            return n
        else:
            return self.gcd(m, n%m)
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        return self.gcd(nums[-1], nums[0])