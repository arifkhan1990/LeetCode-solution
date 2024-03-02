# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {0: [], 1: [TreeNode()]}
        def solve(n):
            if n in dp:
                return dp[n]
            ans = []
            for i in range(n):
                r = n - 1 - i
                left, right = solve(i), solve(r)
                
                for n1 in left:
                    for n2 in right:
                        ans.append(TreeNode(0,n1, n2))
            dp[n] = ans

            return ans
        return solve(n)

