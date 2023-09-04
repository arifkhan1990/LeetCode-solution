class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range (c):
                
                if matrix[i][j] == 0:
                    for x in range(0,r):
                        if matrix[x][j] != 0:
                            matrix[x][j] = '*'

                    for y in range(0,c):
                        if matrix[i][y] != 0:
                            matrix[i][y] = '*'

        for i in range(r):
            for j in range (c):
                if matrix[i][j] == '*':
                    matrix[i][j] = 0

        return matrix

