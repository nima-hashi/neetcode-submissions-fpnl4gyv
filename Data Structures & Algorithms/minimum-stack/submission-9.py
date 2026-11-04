class MinStack:

    def __init__(self):
        self.minStack = [] # (val, min)
        self.curMin = None

    def push(self, val: int) -> None:

        if self.curMin is None:
            self.curMin = val
        
        self.curMin = min(self.curMin, val)
        self.minStack.append([val, self.curMin])
        

    def pop(self) -> None:

        self.minStack.pop()
        if self.minStack:
            self.curMin = self.minStack[-1][1]
        else:
            self.curMin = None
            
        

    def top(self) -> int:

        return self.minStack[-1][0]
        

    def getMin(self) -> int:
        return self.minStack[-1][1]
        
