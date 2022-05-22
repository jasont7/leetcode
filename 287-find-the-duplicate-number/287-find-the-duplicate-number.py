class Solution(object):
    def findDuplicate(self, nums):
        for n in nums:
            if nums[abs(n)] < 0:
                return abs(n)
            else:
                nums[abs(n)] = -nums[abs(n)]