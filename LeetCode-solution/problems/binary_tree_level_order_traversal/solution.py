# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        ans  = []
        if root == None:
            return ans
        nodes = [root]
        while len(nodes) != 0:
            ans.append([node.val for node in nodes])
            next_node = []
            for node in nodes:
                if node.left:
                    next_node.append(node.left)
                if node.right:
                    next_node.append(node.right)
            nodes = next_node
        return ans
        