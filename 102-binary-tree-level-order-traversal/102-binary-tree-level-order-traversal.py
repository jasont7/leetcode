# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if not root: return []
        
        res = []
        q = deque()
        q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if not node: continue
                
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            
            if len(level):
                res.append(level)

        return res