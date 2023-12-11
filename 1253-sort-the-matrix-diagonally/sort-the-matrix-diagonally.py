class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        def sort_diagonal(i, j):
            diagonal_mat = []
            while i < m and j < n:
                diagonal_mat.append(mat[i][j])
                i, j = i + 1, j + 1
            diagonal_mat.sort()
            i, j = i - 1, j - 1
            
            while i >= 0 and j >= 0:
                mat[i][j] = diagonal_mat.pop()
                i, j = i - 1, j - 1

        for i in range(m):
            sort_diagonal(i, 0)
        
        for j in range(1, n):
            sort_diagonal(0, j)
        
        return mat
