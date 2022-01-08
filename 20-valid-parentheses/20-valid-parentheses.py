class Solution:
    def isValid(self, s: str) -> bool:
        pmap = {')':'(', '}':'{', ']':'['}
        
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not len(stack): return False
                
                if stack[-1] == pmap[c]:
                    stack.pop()
                else:
                    return False
        
        return True if not len(stack) else False