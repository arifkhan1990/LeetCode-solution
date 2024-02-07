# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        val1 = root1.val if root1 else 0
        val2 = root2.val if root2 else 0
        root = TreeNode(val1 + val2)
        if root1 and root2:
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
        elif root1:
            root.left = self.mergeTrees(root1.left, None)
            root.right = self.mergeTrees(root1.right, None)
        else:
            root.left = self.mergeTrees(None, root2.left)
            root.right = self.mergeTrees(None, root2.right)

        return root