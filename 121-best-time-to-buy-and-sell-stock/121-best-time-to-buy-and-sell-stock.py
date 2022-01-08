class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMax, totalMax = 0, 0
        for i in range(1, len(prices)):
            curMax = max(0, curMax + prices[i] - prices[i-1])
            totalMax = max(curMax, totalMax)
        return totalMax