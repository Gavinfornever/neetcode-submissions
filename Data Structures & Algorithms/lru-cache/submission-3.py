class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nxt = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left
    
    def insert(self, n):
        n.prev, n.nxt = self.right.prev, self.right
        self.right.prev.nxt = n
        self.right.prev = n

    def remove(self, n):
        prev, nxt = n.prev, n.nxt
        prev.nxt, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        res = -1
        if key in self.cache.keys():
            res = self.cache[key].val
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        return res

    def put(self, key: int, value: int) -> None:
        # if exists the same key
        if key in self.cache.keys():
            self.remove(self.cache[key])
        # insert the key
        n = Node(key, value)
        self.insert(n)
        # add to cache
        self.cache[key] = n
        # del if exceeds capacity
        if self.cap < len(self.cache):
            del self.cache[self.left.nxt.key]
            self.remove(self.left.nxt)







