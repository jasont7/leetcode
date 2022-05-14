class Solution(object):
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        for num in counts:
            if counts[num] > len(nums)//2: 
                return num 