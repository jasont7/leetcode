# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        head = ListNode()
        cur = head
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next
            elif l2.val < l1.val:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next
            else:
                cur.next = ListNode(l1.val)
                cur.next.next = ListNode(l2.val)
                cur = cur.next.next
                l1, l2 = l1.next, l2.next
        cur.next = l1 or l2 
        return head.next