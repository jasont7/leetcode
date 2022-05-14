class Solution(object):
    def containsDuplicate(self, nums):
        counts = {}
        for n in nums:
            if n in counts:
                return True
            else:
                counts[n] = 1
        return False