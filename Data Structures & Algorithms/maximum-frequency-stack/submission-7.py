class FreqStack:

    def __init__(self):
        self.stacks = []
        self.count = {}       

    def push(self, val: int) -> None:

        self.count[val] = 1 + self.count.get(val, 0)

        if self.count[val] > len(self.stacks):
            self.stacks.append([])

        self.stacks[self.count[val] - 1].append(val)

    def pop(self) -> int:

        removed = self.stacks[-1].pop()

        self.count[removed] -= 1

        if not self.stacks[-1]:
            self.stacks.pop()

        return removed

        
        


# Your countStack object will be instantiated and called as such:
# obj = countStack()
# obj.push(val)
# param_2 = obj.pop()