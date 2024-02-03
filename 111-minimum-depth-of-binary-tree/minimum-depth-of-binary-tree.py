# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, ans):
            if node is None:
                return ans

            ans += 1 
            if node.left is None and node.right is None:
                return ans

            l = dfs(node.left, ans)

            r = dfs(node.right, ans)
            
            if node.left is None or node.right is None:
                return max(l,r)
                
            return min(l,r)
        if root == None:
            return 0

        return dfs(root, 0)