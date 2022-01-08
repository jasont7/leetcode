class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diffs = {}
        for idx, num in enumerate(nums):
            diffs[target-num] = idx
        
        for idx, num in enumerate(nums):
            if num in diffs and idx != diffs[num]:
                return [idx, diffs[num]]