class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n,m = len(mat),len(mat[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if sum(mat[i]) == 1:
                        colS = 0
                        for k in range(n):
                            colS += mat[k][j]
                        if colS == 1:
                            ans += 1
        return ans
        