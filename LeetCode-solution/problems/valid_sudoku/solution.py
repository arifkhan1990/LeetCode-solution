class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = []
        
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    if(c+'row'+str(i) not in seen and c+'col'+str(j) not in seen and c+'box'+str(i//3)+str(j//3) not in seen):
                        seen.append(c+'row'+str(i))
                        seen.append(c+'col'+str(j))
                        seen.append(c+'box'+str(i//3)+str(j//3))
                    else:
                        return False
        return True