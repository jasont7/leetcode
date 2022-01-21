# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        preHead = ListNode(next=head)
        front, back = preHead, preHead
        delay = n
        while front.next.next != None:
            front = front.next
            delay -= 1
            if delay <= 0:
                back = back.next
        back.next = back.next.next
        return preHead.next