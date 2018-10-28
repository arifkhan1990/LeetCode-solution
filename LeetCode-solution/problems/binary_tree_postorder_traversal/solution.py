# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        ans = []
        if root:
            ans = self.postorderTraversal(root.left)
            ans = ans + self.postorderTraversal(root.right)
            ans.append(root.val)
        return ans
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        