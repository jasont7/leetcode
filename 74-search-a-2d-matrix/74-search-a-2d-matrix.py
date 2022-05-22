class Solution(object):
    def searchMatrix(self, A, t):
        def findRow():
            left, right = 0, len(A)-1
            while left <= right:
                mid = (left + right) // 2
                if A[mid][0] > t:
                    right = mid-1
                elif A[mid][-1] < t:
                    left = mid+1
                else:
                    return A[mid]
            return None
        
        def searchRow(row):
            left, right = 0, len(row)-1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] > t:
                    right = mid-1
                elif row[mid] < t:
                    left = mid+1
                else:
                    return True
            return False
        
        row = findRow() 
        return searchRow(row) if row else False