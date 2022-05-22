class Solution(object):
    def findMin(self, A):
        l, r = 0, len(A)-1
        while l < r:
            if l == r-1: return min(A[l], A[r])
            
            mid = (r+l)//2
            if A[r] > A[mid]:
                r = mid
            else:
                l = mid
        return A[r]