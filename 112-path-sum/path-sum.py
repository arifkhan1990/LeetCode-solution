# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(r, sm):
            if not r:
                return 0
            
            sm += r.val

            if not r.left and not r.right:
                return sm == targetSum

            return dfs(r.left, sm) or dfs(r.right, sm)

        return dfs(root, 0)