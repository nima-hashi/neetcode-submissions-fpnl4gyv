class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # buy = 0
        # sell = 1

        # while sell < len(prices):
        #     if prices[buy] > prices[sell]:
        #         buy = sell
        #         sell += 1
        #     else:
        #         profit += prices[sell] - prices[buy]
        #         buy += 1
        #         sell += 1   

        # return profit

        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
        
