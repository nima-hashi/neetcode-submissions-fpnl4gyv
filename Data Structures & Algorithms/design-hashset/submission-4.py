class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.set = [[] for i in range(self.size)]
        
    def add(self, key: int) -> None:
        k = key % self.size
        if key not in self.set[k]:
            self.set[k].append(key)
        
    def remove(self, key: int) -> None:
         k = key % self.size
         if key in self.set[k]:
            self.set[k].remove(key)

    def contains(self, key: int) -> bool:
         k = key % self.size
         if key in self.set[k]:
            return True
         return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)