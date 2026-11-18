class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        profit = 0

        while r < len(prices):
            curProfit = prices[r] - prices[l]
            if curProfit > 0:
                profit = max(profit, curProfit)
            else:
                l = r
            r += 1
        return profit
        