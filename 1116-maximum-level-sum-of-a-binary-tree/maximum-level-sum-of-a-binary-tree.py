# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        l_s = []  # Initialize l_s with 0 for the root level
            
        def dfs(node, l):
            if not node:
                return
            
            # Ensure l_s has enough elements to accommodate the level
            if len(l_s) == l:
                l_s.append([])
                
            dfs(node.left, l + 1)
            l_s[l].append(node.val)
            dfs(node.right, l + 1)

        dfs(root, 0)
        mxs =[sum(x) for x in l_s]
        return 1 + mxs.index(max(mxs))