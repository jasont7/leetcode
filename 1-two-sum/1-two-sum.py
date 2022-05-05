class Solution(object):
    def twoSum(self, nums, target):
        diffs = {}
        for idx, n in enumerate(nums):
            diffs[target-n] = idx
        
        for idx, n in enumerate(nums):
            if n in diffs and idx != diffs[n]:
                return [idx, diffs[n]]
        