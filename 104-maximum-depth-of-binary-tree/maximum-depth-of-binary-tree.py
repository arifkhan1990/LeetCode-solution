# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, ans):
            if node is None:
                return ans
            ans += 1 
            return max(dfs(node.left, ans), dfs(node.right, ans))

        if root == None:
            return 0

        return dfs(root, 0)