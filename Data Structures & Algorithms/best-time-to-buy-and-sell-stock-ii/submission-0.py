class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        if len(prices) == 0:
            return profit
    
        buy = 0
        sell = 1
        possible = 0

        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
                sell += 1
            else:
                profit += prices[sell] - prices[buy]
                buy = sell
                sell += 1
        return profit
        
