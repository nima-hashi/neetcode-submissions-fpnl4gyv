class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0

        while r < len(prices):
            curProfit = prices[r] - prices[l]
            if curProfit > 0:
                maxProfit = max(maxProfit, curProfit)
            else:
                l = r
            r += 1
        return maxProfit
        