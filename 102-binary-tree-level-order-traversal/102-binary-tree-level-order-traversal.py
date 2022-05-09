# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root: return []
        
        res = []
        q = [root]
        while len(q):
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                if not node: continue
                
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            
            if len(level):
                res.append(level)

        return res