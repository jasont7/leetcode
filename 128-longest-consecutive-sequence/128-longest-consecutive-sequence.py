class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in nums:
                k = n+1
                while k in nums:
                    k += 1
                longest = max(longest, k-n)
        return longest