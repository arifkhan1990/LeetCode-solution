# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        def travel(node):
            if node is None:
                return 0
            
            left = travel(node.left)
            right = travel(node.right)
            self.cnt += abs(left) + abs(right)
            return node.val + left + right - 1
        
        travel(root)
        return self.cnt
