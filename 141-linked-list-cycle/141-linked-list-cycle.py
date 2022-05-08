class Solution(object):
    def hasCycle(self, head):
        if not head: return False
        
        slow_ptr = head
        fast_ptr = head.next
        while fast_ptr:
            if slow_ptr == fast_ptr:
                return True
            if not fast_ptr.next:
                return False
            
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        
        return False