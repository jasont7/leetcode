class Solution(object):
    def findMin(self, A):
        l, r = 0, len(A)-1
        while l < r:
            mid = (r+l)//2
            if A[mid] > A[r]:
                l = mid+1
            else:
                r = mid
        return A[l]