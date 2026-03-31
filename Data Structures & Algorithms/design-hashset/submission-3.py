class MyHashSet:

    def __init__(self):
        self.bucket_size = 1000
        self.buckets = [[] for _ in range(self.bucket_size)]
        

    def add(self, key: int) -> None:
        bucket_index = key % self.bucket_size
        if key not in self.buckets[bucket_index]:
            self.buckets[bucket_index].append(key)
        

    def remove(self, key: int) -> None:
        bucket_index = key % self.bucket_size
        if key in self.buckets[bucket_index]:
            self.buckets[bucket_index].remove(key)
        

    def contains(self, key: int) -> bool:
        bucket_index = key % self.bucket_size
        return key in self.buckets[bucket_index]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)