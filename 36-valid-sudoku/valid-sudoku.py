class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = {}
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                seen[c+'row'+str(i)] = 0
                seen[c+'col'+str(j)] = 0
                seen[c+'box'+str(i//3)+str(j//3)] = 0

        
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c != '.':
                    if(seen[c+'row'+str(i)] != 1 and seen[c+'col'+str(j)] != 1 and seen[c+'box'+str(i//3)+str(j//3)] != 1):
                        seen[c+'row'+str(i)] = 1
                        seen[c+'col'+str(j)] = 1
                        seen[c+'box'+str(i//3)+str(j//3)] = 1
                    else:
                        return False
        return True