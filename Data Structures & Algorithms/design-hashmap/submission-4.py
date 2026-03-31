class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.bucket = [ListNode(0,0) for i in range(self.size)]

    def put(self, key: int, value: int) -> None:
        i = key % self.size
        cur = self.bucket[i]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key,value)

    def get(self, key: int) -> int:
        i = key % self.size
        cur = self.bucket[i]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1
        
    def remove(self, key: int) -> None:
        i = key % self.size
        cur = self.bucket[i]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)