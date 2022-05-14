class Solution(object):
    def majorityElement(self, nums):
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        for n in d:
            if d[n] > len(nums)//2: 
                return n