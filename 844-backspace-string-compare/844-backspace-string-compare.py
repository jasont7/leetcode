class Solution(object):
    def backspaceCompare(self, s, t):
        s_stack = []
        for char in s:
            if char == '#' and s_stack:
                s_stack.pop()
            elif char != '#':
                s_stack.append(char)
        
        t_stack = []
        for char in t:
            if char == '#' and t_stack:
                t_stack.pop()
            elif char != '#':
                t_stack.append(char)
        
        return s_stack == t_stack