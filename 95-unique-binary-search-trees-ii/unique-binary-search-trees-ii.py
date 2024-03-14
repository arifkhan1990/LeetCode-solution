# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def solve(l, r):
            if l == r:
                return [TreeNode(l)]
            if l > r:
                return [None]
            
            ans = []

            for i in range(l, r+1):
                for ln in solve(l, i - 1):
                    for rn in solve(i+1, r):
                        root = TreeNode(i, ln, rn)
                        ans.append(root)
            return ans
        return solve(1, n)