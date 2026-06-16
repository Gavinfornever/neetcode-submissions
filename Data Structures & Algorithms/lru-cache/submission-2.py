class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)  
        self.left.nxt = self.right
        self.right.prev = self.left
        self.capacity = capacity

    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.nxt = nxt.prev = node
        node.nxt, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache.keys():
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        # if exists, remove and insert
        if key in self.cache.keys():
            self.remove(self.cache[key])
        self.insert(node)
        self.cache[key] = node
        # if exceeds capacity, remove the last one
        if len(self.cache) > self.capacity:
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]



