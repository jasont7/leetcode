# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        slow, fast = head, head.next
        while True:
            if not fast: return slow
            slow = slow.next
            fast = fast.next if not fast.next else fast.next.next