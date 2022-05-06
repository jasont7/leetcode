class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            pivot = left + (right-left)//2
            if nums[pivot] == target:
                return pivot
            elif target > nums[pivot]:
                left = pivot + 1
            elif target < nums[pivot]:
                right = pivot - 1
        return -1