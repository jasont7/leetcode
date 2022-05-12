class Solution(object):
    def insert(self, intervals, newI):
        left, right = [], []
        for I in intervals:
            if I[1] < newI[0]:
                left.append(I)
            elif I[0] > newI[1]:
                right.append(I)
            else:
                newI[0] = min(newI[0], I[0])
                newI[1] = max(newI[1], I[1])
                
        return left + [newI] + right