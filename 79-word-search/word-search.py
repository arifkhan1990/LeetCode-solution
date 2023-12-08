class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, k):
            if not (0 <= i < len(board) and 0 <= j < len(board[0])) or board[i][j] != word[k]:
                return 0
            
            if k == len(word) - 1:
                return 1
            
            tmp, board[i][j] = board[i][j], '/'

            ans = (backtrack(i+1, j, k+1) or backtrack(i-1,j,k+1) or 
                    backtrack(i, j+1, k+1) or backtrack(i,j-1, k+1))
            board[i][j] = tmp

            return ans
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return 1
        return 0