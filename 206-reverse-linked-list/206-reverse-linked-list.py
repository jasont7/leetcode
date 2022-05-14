# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if not head: return head
        
        l, m, r = None, head, head.next
        while m: 
            m.next = l
            l, m = m, r
            if r: r = r.next
        return l