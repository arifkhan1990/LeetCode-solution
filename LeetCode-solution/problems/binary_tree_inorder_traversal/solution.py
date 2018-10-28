# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        ans = []
        if root:
            ans = self.inorderTraversal(root.left)
            ans.append(root.val)
            ans = ans + self.inorderTraversal(root.right)
        return ans