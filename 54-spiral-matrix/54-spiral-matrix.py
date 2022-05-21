class Solution(object):
    def spiralOrder(self, A):
        m, n = len(A), len(A[0])
        
        res = []
        
        top, left = 0, 0
        bottom, right = len(A)-1, len(A[0])-1
        while True:
            for i in range(left, right+1):
                res.append(A[top][i])
            top += 1
            if len(res) == n*m: break
            
            for i in range(top, bottom+1):
                res.append(A[i][right])
            right -= 1
            if len(res) == n*m: break
            
            for i in range(right, left-1, -1):
                res.append(A[bottom][i])
            bottom -= 1
            if len(res) == n*m: break
            
            for i in range(bottom, top-1, -1):
                res.append(A[i][left])
            left += 1
            if len(res) == n*m: break 
            
        return res