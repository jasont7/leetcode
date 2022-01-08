class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while (lo < hi):
            mid = (hi + lo) // 2
            if nums[mid] > nums[hi]:
                lo = mid+1
            else:
                hi = mid
        
        a = self.binary_search(nums, lo, len(nums)-1, target)
        b = self.binary_search(nums, 0, lo-1, target)
        return max(a, b)
    
    def binary_search(self, A, lo, hi, t):
        if hi >= lo:
            mid = (hi + lo) // 2
            if A[mid] == t:
                return mid
            elif A[mid] > t:
                return self.binary_search(A, lo, mid-1, t)
            else:
                return self.binary_search(A, mid+1, hi, t)
        else:
            return -1