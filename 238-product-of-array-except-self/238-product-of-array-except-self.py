class Solution(object):
    def productExceptSelf(self, nums):
        res = []
        
        p = 1
        for i in range(0, len(nums)):
            res.append(p)
            p = p * nums[i]
        
        p = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * p
            p = p * nums[i]
        
        return res 