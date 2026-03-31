class ListNode:

    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.set = [ListNode(0) for i in range(self.size)]
        
    def add(self, key: int) -> None:
        i = key % self.size
        # if key not in self.set[i]:
        #     self.set[i].append(key)

        cur = self.set[i]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)
        
    def remove(self, key: int) -> None:
        i = key % self.size

        cur = self.set[i]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


    def contains(self, key: int) -> bool:
        i = key % self.size
        cur = self.set[i]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)