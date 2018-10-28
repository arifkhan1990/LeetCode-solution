# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        ans = []
        if root:
            ans.append(root.val)
            ans = ans + self.preorderTraversal(root.left)
            ans = ans + self.preorderTraversal(root.right)
        return ans
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        