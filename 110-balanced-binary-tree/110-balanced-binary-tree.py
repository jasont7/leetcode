# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        return self.dfsHeight(root) != -1
        
    def dfsHeight(self, node):
        if not node: return 0
        
        leftH = self.dfsHeight(node.left)
        if leftH == -1:
            return -1
        
        rightH = self.dfsHeight(node.right)
        if rightH == -1:
            return -1
        
        if abs(leftH - rightH) > 1: 
            return -1
        return max(leftH, rightH) + 1