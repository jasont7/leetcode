class Solution(object):
    def searchRange(self, A, t):
        
        def getEnd():
            left, right = 0, len(A)-1
            while left <= right:
                mid = (left + right)//2
                if A[mid] > t:
                    right = mid-1
                elif A[mid] < t:
                    left = mid+1
                else:
                    if mid == len(A)-1 or A[mid+1] > t:
                        return mid
                    else:
                        left = mid+1
            return -1
        
        def getStart():
            left, right = 0, len(A)-1
            while left <= right:
                mid = (left + right)//2
                if A[mid] > t:
                    right = mid-1
                elif A[mid] < t:
                    left = mid+1
                else:
                    if mid == 0 or A[mid-1] < t:
                        return mid
                    else:
                        right = mid-1
            return -1
        
        return [getStart(), getEnd()]