class FreqStack:

    def __init__(self):
        self.stacks = []
        self.count = {}        

    def push(self, val: int) -> None:
        self.count[val] = self.count.get(val, 0) + 1
        if self.count[val] > len(self.stacks):
            self.stacks.append([])
        self.stacks[self.count[val] - 1].append(val)

    def pop(self) -> int:
        for i in range(len(self.stacks)-1, -1, -1):
            if self.stacks[i]:
                popped = self.stacks[i].pop()
                self.count[popped] -= 1
                return popped
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()