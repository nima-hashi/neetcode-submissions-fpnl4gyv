from collections import deque
class RecentCounter:

    def __init__(self):

        self.q = deque()
        

    def ping(self, t: int) -> int:

        leftRange = t - 3000

        while self.q and self.q[0] < leftRange:
            self.q.popleft()
        self.q.append(t)

        return len(self.q)
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)