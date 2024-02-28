# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        left_node_val = 0
        mx_lavel = -1 
        def dfs(node, lavel):
            nonlocal mx_lavel, left_node_val
            if not node:
                return
            
            if mx_lavel < lavel:
                mx_lavel = lavel
                left_node_val = node.val

            dfs(node.left, lavel + 1)
            dfs(node.right, lavel + 1)

        dfs(root, 0)

        return left_node_val