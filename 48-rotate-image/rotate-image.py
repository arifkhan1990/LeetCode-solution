class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ans = []
        for i in range(len(matrix)):
            x = []
            for j in range(len(matrix[0])):
                x.append(matrix[j][i])
            ans.append(x[::-1])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = ans[i][j]
        

        