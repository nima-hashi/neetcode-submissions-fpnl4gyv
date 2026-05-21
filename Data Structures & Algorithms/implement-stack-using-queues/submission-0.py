class MyStack:

    [1,2,3,4,5,1,2,3,4,]

    def __init__(self):
        self.q = []
        
    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        size = len(self.q) - 1
        for i in range(size):
            self.q.append(self.q.pop(0))
        return self.q.pop(0)
        

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        return self.q == []
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()