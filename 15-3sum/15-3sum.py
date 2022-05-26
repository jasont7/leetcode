class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        
        res = []
        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            target = -nums[i]
            lo, hi = i+1, len(nums)-1
            while lo < hi:
                if nums[lo] + nums[hi] == target:
                    res.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi-1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif nums[lo] + nums[hi] < target:
                    lo += 1
                else:
                    hi -= 1
        
        return res