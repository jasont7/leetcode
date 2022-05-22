# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            n += 1
            cur = cur.next
        
        cur = head
        i = 0
        while i < n//2:
            new = stack.pop()
            new.next = cur.next
            cur.next = new
            
            i += 1
            cur = cur.next.next
        cur.next = None