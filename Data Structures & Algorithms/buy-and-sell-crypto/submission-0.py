class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        m = 0

        buy, sell = 0, 1

        while sell < len(prices):
            if prices[buy] >= prices[sell]:
                buy = sell
                sell += 1
            
            else:
                m = max(m, prices[sell] - prices[buy])
                sell += 1
        
        return m

