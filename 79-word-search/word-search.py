class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        path = set()

        def search(row, col, idx):
            if idx == len(word):
                return 1
            
            if (row < 0 or col < 0 or row >= r or col >= c or word[idx] != board[row][col] or (row, col) in path ):
                return 0
            
            path.add((row, col))
            ans = (search(row + 1, col, idx + 1) or
                   search(row - 1, col, idx + 1) or 
                   search(row, col + 1, idx + 1) or
                   search(row, col - 1, idx + 1))
            path.remove((row, col))
            return ans
        
        for row in range(r):
            for col in range(c):
                if search(row, col, 0):
                    return 1
        return 0