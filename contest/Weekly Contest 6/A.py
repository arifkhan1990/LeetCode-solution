# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def solve(root, l):
            if not root:
                return
            
            if root.left:
                if not root.left.left and not root.left.right:
                    l.append(root.left.val)
            
            solve(root.left, l)
            solve(root.right, l)
            return l
        return sum(solve(root, []))