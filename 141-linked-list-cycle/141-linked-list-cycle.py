# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def hasCycle(self, head):
        seen = {}
        
        node = head
        while node:
            if node in seen:
                return True
            seen[node] = 1
            node = node.next
            
        return False