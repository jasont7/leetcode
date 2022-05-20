class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                r = stack.pop()
                l = stack.pop()
                if t == '+':
                    stack.append(int(l) + int(r))
                elif t == '-':
                    stack.append(int(l) - int(r))
                elif t == '*':
                    stack.append(int(l) * int(r))
                elif t == '/':
                    stack.append(int(float(l)/r))
        
        return stack.pop()