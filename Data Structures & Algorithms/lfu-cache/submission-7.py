class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 1

class DoublyLinkedList:

    def __init__(self):

        self.left = ListNode(0,0)
        self.right = ListNode(0,0)

        self.left.next = self.right
        self.right.prev = self.left

        self.size = 0
    
    def remove(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1
    
    def insert(self, node):

        node.prev = self.right.prev
        node.next = self.right

        self.right.prev.next = node
        self.right.prev = node

        self.size += 1
    
    def removeLRU(self):

        if self.size == 0:
            return None
        
        lru = self.left.next
        self.remove(lru)
        return lru
        

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> node
        self.valMap = {} # frequency -> doubly linked list
        self.minFreq = 0 # Minimum frequency in cache

    def updateFreq(self, node):
        freq = node.freq

        self.valMap[freq].remove(node)

        if self.minFreq == freq and self.valMap[freq].size == 0:
            self.minFreq += 1
        
        node.freq += 1

        if node.freq not in self.valMap:
            self.valMap[node.freq] = DoublyLinkedList()
        self.valMap[node.freq].insert(node)

    def get(self, key: int) -> int:

        if key not in self.cache:
            return - 1

        node = self.cache[key]
        self.updateFreq(node)

        return node.val

        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.updateFreq(node)
            return
        
        if len(self.cache) >= self.capacity:
           
           lruList = self.valMap[self.minFreq] 
           lru = lruList.removeLRU()
           del self.cache[lru.key]
        
        node = ListNode(key, value)
        self.cache[key] = node
        if 1 not in self.valMap:
            self.valMap[1] = DoublyLinkedList()
        self.valMap[1].insert(node)

            # New nodes always have frequency 1
        self.minFreq = 1



        
    

        

    


            



        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)