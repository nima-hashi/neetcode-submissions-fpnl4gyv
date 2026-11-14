class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit += prices[sell] - prices[buy]
            buy = sell
            sell += 1
        return profit
        