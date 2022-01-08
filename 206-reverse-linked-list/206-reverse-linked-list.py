# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    
#     # Recursive
#     def reverseList(self, curr, prev=None):
#         if curr is None:
#             return prev
        
#         new = curr.next
#         curr.next = prev
#         return self.reverseList(curr=new, prev=curr)
    
    
    # Iterative
    def reverseList(self, curr):
        prev = None
        while curr:
            new = curr.next
            curr.next = prev
            prev, curr = curr, new
        return prev
