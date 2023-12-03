class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        cell, c = n*n, 1

        
        l,r,t,b = 0, n, 0, n

        while l < r and t < b:

            for i in range(l,r):
                matrix[t][i] = c
                c += 1
            t += 1

            for i in range(t, b):
                matrix[i][r-1] = c
                c += 1
            r -= 1

            if not (l < r and t < b):
                break

            for i in range(r-1, l-1, -1):
                matrix[b-1][i] = c
                c += 1
            b -= 1

            for i in range(b-1, t-1, -1):
                matrix[i][l] = c
                c += 1
            l += 1
        return matrix
        