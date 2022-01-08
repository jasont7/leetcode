class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        triplets = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:  # skip repeat targets
                continue

            # we want to keep these two pointers ahead of the target
            # so as not to have a repeating sequence of pointers.
            l, r = i+1, len(nums)-1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]  # nums[i] is the target
                
                if   s < 0: l += 1
                elif s > 0: r -= 1
                elif s == 0:
                    triplets.append([nums[i], nums[l], nums[r]])
                    
                    # skip repeat numbers for the given target
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        
        return triplets