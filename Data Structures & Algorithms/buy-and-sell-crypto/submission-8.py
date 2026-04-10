class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        buy = 0

        for sell in range(1, len(prices)):
            if prices[buy] > prices[sell]:
                buy = sell
                #sell += 1
            else:
                profit = max(profit, prices[sell] - prices[buy])
            sell += 1
        return profit

    
        