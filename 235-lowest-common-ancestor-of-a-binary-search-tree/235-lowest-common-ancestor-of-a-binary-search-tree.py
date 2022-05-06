# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        lca = root
        while True:
            if (p.val <= lca.val and q.val >= lca.val) or (p.val >= lca.val and q.val <= lca.val):
                return lca
            elif p.val < lca.val and q.val < lca.val:
                lca = lca.left
            else:
                lca = lca.right
            
        