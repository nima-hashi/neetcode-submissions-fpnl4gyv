class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Best Time to Buy and Sell Stock II

        # profit = 0
        # buy = 0
        # sell = 1

        # while sell < len(prices):
        #     possibleProfit = 0
        #     if prices[buy] > prices[sell]:
        #         buy = sell
        #     else:
        #         profit = max(profit, prices[sell] - prices[buy])
        #     sell += 1
        # return profit




        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit