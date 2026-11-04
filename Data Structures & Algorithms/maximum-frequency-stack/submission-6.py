class FreqStack:

    def __init__(self):
        self.stacks = []
        self.count = {}   
        self.maxCount = 0     

    def push(self, val: int) -> None:
        self.count[val] = self.count.get(val, 0) + 1
        self.maxCount = max(self.maxCount, self.count[val])
        if self.count[val] > len(self.stacks):
            self.stacks.append([])
        self.stacks[self.count[val] - 1].append(val)

    def pop(self) -> int:
        popped = self.stacks[self.maxCount - 1].pop()
        self.count[popped] -= 1
        if not self.stacks[self.maxCount-1]:
            self.maxCount -= 1
        return popped
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()