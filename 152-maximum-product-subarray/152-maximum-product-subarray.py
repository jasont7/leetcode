class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        rollingMax, rollingMin = 1, 1
        
        for n in nums:
            vals = [n, n*rollingMax, n*rollingMin]
            rollingMax = max(vals)
            rollingMin = min(vals)
            
            if rollingMax > res:
                res = rollingMax
        
        return res