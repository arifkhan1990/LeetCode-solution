class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        n = len(mat)
        for i in range(n):
            k = mat[i]
            ans += k[i] + k[-(i+1)]
        if n > 1:
            if n&1:
                ans -= mat[n//2][n//2]
        else:
            ans = mat[0][0]
        
        return ans