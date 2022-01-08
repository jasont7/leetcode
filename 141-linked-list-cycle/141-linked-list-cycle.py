# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # O(1) space alg
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast: 
                return True
        return False
    
    
    # # O(n) space alg
    # def hasCycle(self, curr):
    #     seen = {}
    #     while curr and curr.next:
    #         if curr.next.val in seen and seen[curr.next.val] == curr.next:
    #             return True
    #         seen[curr.val] = curr
    #         curr = curr.next
    #     return False
        