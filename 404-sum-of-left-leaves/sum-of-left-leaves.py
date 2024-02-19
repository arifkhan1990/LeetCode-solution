# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            if node.left and not node.left.left and not node.left.right:
                left_leaf_value = node.left.val
            else:
                left_leaf_value = 0

                

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            return left_leaf_value + left_sum + right_sum

        return dfs(root)
