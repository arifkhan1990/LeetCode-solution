class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        sL = [[1]*i for i in range(1,numRows+1)]
        for i in range(1,numRows):
            for j in range(1,len(sL[i-1])):
                sL[i][j] =  sL[i-1][j-1] + sL[i-1][j]
        return sL
        