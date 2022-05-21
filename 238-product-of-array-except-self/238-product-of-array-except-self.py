class Solution(object):
    def productExceptSelf(self, nums):
        res = []
        
        pref = 1
        for i in range(0, len(nums)):
            res.append(pref)
            pref = pref * nums[i]
        
        suf = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * suf
            suf = suf * nums[i]
        
        return res 