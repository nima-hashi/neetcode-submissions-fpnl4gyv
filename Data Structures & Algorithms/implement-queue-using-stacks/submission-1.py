class MyQueue:

    def __init__(self):
        self.stack = []
        self.popFrom = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        if self.popFrom:
            return self.popFrom.pop()
        else:
            while self.stack:
                self.popFrom.append(self.stack.pop())
            return self.popFrom.pop()
        

    def peek(self) -> int:
        if self.popFrom:
            return self.popFrom[-1]
        else:
            while self.stack:
                self.popFrom.append(self.stack.pop())
            return self.popFrom[-1]

        

    def empty(self) -> bool:
        return not self.stack and not self.popFrom
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()