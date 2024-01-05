class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for i in range(1,n+1):
            ans[i] = (i&1) + ans[i//2]
        return ans