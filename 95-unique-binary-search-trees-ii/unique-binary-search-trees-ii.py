# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}
        def solve(l, r):
            if l > r:
                return [None]
            
            if (l, r) in dp:
                return dp[(l,r)]
            ans = []

            for i in range(l, r+1):
                for ln in solve(l, i - 1):
                    for rn in solve(i+1, r):
                        root = TreeNode(i, ln, rn)
                        ans.append(root)
            dp[(l,r)] = ans
            return ans
        return solve(1, n)