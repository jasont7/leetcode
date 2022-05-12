# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        parents = {}
        def dfsGetParents(node):
            if node.left:
                parents[node.left] = node
                dfsGetParents(node.left)
            if node.right:
                parents[node.right] = node
                dfsGetParents(node.right)
        
        dfsGetParents(root)
        
        p_ancestors = []
        curr = p
        while True:
            p_ancestors.append(curr)
            if curr == root: break
            
            curr = parents[curr]
        
        curr = q
        while curr != root:
            if curr in p_ancestors:
                return curr
            curr = parents[curr]
        return root