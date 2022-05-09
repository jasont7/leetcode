class Solution(object):
    def shipWithinDays(self, weights, D):
        # checks if capacity can be shipped in D days 
        def feasible(capacity):
            days = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:
                    total = weight
                    days += 1
                    if days > D:
                        return False
            return True
        
        # binary search to find minimal feasible capacity
        # max(weights) is the minimum possible capacity
        # sum(weights) is the maximum possible capacity
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right-left) // 2
            if feasible(mid):
                right = mid  # any capacity greater than mid is feasible
            else:
                left = mid + 1  # any capacity less than mid is not feasible
        return left