class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity
        self.DLL = DoublyLinkedList()
        self.hash = {}

    def get(self, key: int) -> int:
        #return key else -1 
        if key not in self.hash: 
            return -1 
        self.DLL.remove(self.hash[key])
        self.hash[key] = self.DLL.push(self.hash[key])
        return self.hash[key].val

    def put(self, key: int, value: int) -> None:

        #update key if key exist 
        if key in self.hash:
            self.DLL.remove(self.hash[key])

        #k-v pair to the cache 
        newNode = Node(key,value)
        self.hash[key] = self.DLL.push(newNode)

        #if exceeds the capacity,evict the least recently used key
        if self.DLL.length > self.capacity: 
            lru = self.DLL.head.next 
            del self.hash[lru.key]
            self.DLL.remove(lru)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node: 
    def __init__(self,key,val):
        self.key = key
        self.val = val 
        self.prev = None
        self.next = None


class DoublyLinkedList: 
    def __init__(self):
        self.length = 0
        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next = self.tail 
        self.tail.prev = self.head

    def remove(self,node):
        prev = node.prev
        nxt = node.next 

        prev.next = nxt 
        nxt.prev = prev

        self.length -= 1

    def push(self, node):
        prev = self.tail.prev
        nxt = self.tail

        prev.next = node 
        nxt.prev = node 

        node.next = nxt 
        node.prev = prev 

        self.length += 1 

        return node