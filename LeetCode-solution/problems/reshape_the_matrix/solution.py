class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        matrix = []*r
        
        arr = [0]*(r*c)
        k = 0

        if r*c != len(mat) * len(mat[0]):
            return mat
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                arr[k] = mat[i][j]
                k += 1
        k = 0
        for l in range(0,r):
            mr = [0]*c
            for p in range(0,c):
                mr[p] = arr[k]
                k += 1
            matrix.append(mr)
        return matrix