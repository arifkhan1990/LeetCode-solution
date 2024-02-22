# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def solve(node, val, depth, l):
            if not node:
                return
            
            if l == depth-1:
                l_node = TreeNode(val)
                l_node.left = node.left
                node.left = l_node

                r_node = TreeNode(val)
                r_node.right = node.right
                node.right = r_node
                return
            solve(node.left, val, depth, l+1)
            solve(node.right, val, depth, l+1)

        if depth == 1:
            n_root = TreeNode(val)
            n_root.left = root
            return n_root
        solve(root, val, depth, 1)
        return root