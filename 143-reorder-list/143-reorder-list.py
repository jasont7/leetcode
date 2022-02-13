# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        n = 0
        p = head
        while p.next:
            n += 1
            p = p.next
        
        t1, t2 = head, head.next
        i = 0
        while t2:
            if i == n//2:
                t1.next = None
                break
            t1, t2 = t2, t2.next
            i += 1
        
        L1 = head
        L2 = self.reverse(t2)
        
        # while L1:
        #     print(L1.val)
        #     L1 = L1.next
        # print('')
        # while L2:
        #     print(L2.val)
        #     L2 = L2.next
        
        return self.merge(L1, L2)
    
    def reverse(self, head):
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre, cur = cur, tmp
        return pre
    
    def merge(self, a, b):
        dummy = ListNode()
        tail = dummy

        while True:
            if a is None:
                tail.next = None
                break
            elif b is None:
                tail.next = a
                break
            else:
                tail.next = a
                tail = a
                a = a.next

                tail.next = b
                tail = b
                b = b.next

        a = dummy.next
        return a

    
    
    
        