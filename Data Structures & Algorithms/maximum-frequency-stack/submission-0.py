class FreqStack:

    def __init__(self):
        self.stack = [] # [5,7,5,7,4,5]
        self.count = {} # {5:3, 7:2, 4:1}

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.count[val] = self.count.get(val, 0) + 1
        

    def pop(self) -> int:

        tempStack = []
        m = max(self.count.values())

        looking = True
        while looking:
            if self.count[self.stack[-1]] == m:
                popped = self.stack.pop()
                while tempStack:
                    self.stack.append(tempStack.pop())
                self.count[popped] = self.count.get(popped, 0) - 1
                return popped
            tempStack.append(self.stack.pop())



        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()