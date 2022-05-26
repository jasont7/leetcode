# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        self.k = k
        self.res = None
        
        def dfs(node):
            if node:
                dfs(node.left)
                self.k -= 1
                if self.k == 0: self.res = node.val
                dfs(node.right)
        
        dfs(root)
        return self.res 