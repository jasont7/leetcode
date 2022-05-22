class Solution(object):
    def search(self, nums, target):
        # binary search to find min element -> O(logn)
        left, right = 0, len(nums)-1
        while left < right:
            mid = (right + left)//2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        min_idx = left
        
        # binary search to find target
        if target <= nums[-1]:
            left, right = min_idx, len(nums)-1
        else:
            left, right = 0, min_idx-1
        while left < right:
            mid = (right + left)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left if nums[left] == target else -1