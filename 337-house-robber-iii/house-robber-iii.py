# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            if not node:
                return (0, 0)
            
            l = solve(node.left)
            r = solve(node.right)

            take = node.val + l[1] + r[1]
            notTake = max(l[0],l[1]) + max(r[0], r[1])
            return (take, notTake)
        ans = solve(root)
        return max(ans[0], ans[1])