class StockSpanner:

    def __init__(self):
        self.stack = []
        self.span = []
        

    def next(self, price: int) -> int:
        if not self.stack or price < self.stack[-1]:
            self.stack.append(price)
            self.span.append(1)
            return 1
        
        curSpan = 0
        while self.stack and self.stack[-1] <= price:
            self.stack.pop()
            curSpan += self.span.pop()
        
        self.stack.append(price)
        self.span.append(curSpan+1)
        return curSpan + 1

        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)