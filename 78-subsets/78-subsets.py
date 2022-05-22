class Solution(object):
    def subsets(self, nums):
        result = [[]]
        for n in nums:
            result += [curr + [n] for curr in result]
        return result