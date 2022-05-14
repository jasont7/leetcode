# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        m = 0
        def maxDepth(node):
            if not node: return 0
            
            left = maxDepth(node.left)
            right = maxDepth(node.right)
            
            nonlocal m
            m = max(m, left+right)
            
            return 1 + max(left, right)
        
        maxDepth(root)
        return m