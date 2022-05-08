class Solution(object):
    def hasCycle(self, head):
        if not head: return False
        
        slow_ptr = head
        fast_ptr = head
        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr: return True
        
        return False