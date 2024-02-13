# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, rs, ps):
            if not node:
                return 0
            
            rs += node.val
            cnt = ps.get(rs - targetSum, 0)
            ps[rs] = ps.get(rs, 0)+1
            
            cnt += dfs(node.left, rs, ps)
            cnt += dfs(node.right, rs, ps)

            ps[rs] -= 1

            return cnt
        return dfs(root, 0, {0:1})