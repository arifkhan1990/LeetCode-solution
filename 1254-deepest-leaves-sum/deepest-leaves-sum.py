# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return []
        
        s = [(root, 0)]
        mxl = -1
        ans = []

        while s:
            node, l = s.pop(0)

            if l > mxl:
                mxl = l
                ans = [node.val]
            else:
                ans.append(node.val)
            
            if node.left:
                s.append((node.left,l+1))
            if node.right:
                s.append((node.right, l+1))
        
        return sum(ans)