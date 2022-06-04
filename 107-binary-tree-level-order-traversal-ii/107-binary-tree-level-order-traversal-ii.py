# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def levelOrderBottom(self, root):
        if not root: return []
        
        result = []
        q = deque([root])
        while q:
            level = []
            
            # process level
            for _ in range(len(q)):
                cur = q.popleft() 
                level.append(cur.val)
                
                if cur.left:  q.append(cur.left)
                if cur.right: q.append(cur.right)
                    
            result.append(level)
            
        return reversed(result)