class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        if not self.stack or self.stack[-1] > price:
            self.stack.append(price)
            return 1
        
        span = 0
        tempStack = []

        while self.stack and self.stack[-1] <= price:
            span += 1
            tempStack.append(self.stack.pop())
        
        while tempStack:
            self.stack.append(tempStack.pop())
        self.stack.append(price)
        
        return span + 1
        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)