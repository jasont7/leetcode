# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sameTree(self, p, q):
        if p and q:
            return p.val == q.val and \
                self.sameTree(p.left, q.left) and \
                self.sameTree(p.right, q.right)
        return p == q
    
    def isSubtree(self, root, subRoot):
        if not root: return
        
        result = False
        if root.val == subRoot.val:
            result = self.sameTree(root, subRoot) 
            
        return True if result else self.isSubtree(root.left, subRoot) or \
                                   self.isSubtree(root.right, subRoot) 