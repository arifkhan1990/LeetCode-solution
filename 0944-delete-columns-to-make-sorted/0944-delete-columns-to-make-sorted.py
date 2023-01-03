class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        num_columns = len(strs[0])
        num_deleted = 0
        for c in range(num_columns):
            for r in range(1, len(strs)):
                if strs[r][c] < strs[r-1][c]:
                    num_deleted += 1
                    break
        return num_deleted