class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nxt = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.first = Data(0, 0)
        self.last = Data(0, 0)
        self.first.nxt = self.last
        self.last.prev = self.first
        self.cache = {}

    ## 对链表的操作
    def delete(self, node) -> None:
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev      

    def insert(self, newData) -> None:
        # if self.first == None:
        #     self.first = self.last = newData
        # else:
        newData.nxt = self.first.nxt
        newData.prev = self.first
        self.first.nxt.prev = newData
        self.first.nxt = newData

    ## 对链表的操作

    # delete key and insert to first
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        tmp = self.cache[key]
        self.delete(tmp)
        self.insert(tmp)
        return self.cache[key].value

    # insert, if exceed: delete last
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 更新
            newData = self.cache[key]
            newData.value = value
            self.delete(newData)
            self.insert(newData)
        else:
            if len(self.cache)==self.cap:
                # 删了最后的元素
                lru = self.last.prev
                self.delete(lru)
                del self.cache[lru.key]
            newData = Data(key, value)
            self.cache[key] = newData
            self.insert(newData)
        # newData = Data(key, value)
        # self.cache[key] = newData
        # self.insert(newData)
        # if len(self.cache)>self.cap:
        #     del self.cache[self.last.prev.key]
        #     self.delete(self.last.prev)

        # print("-----")
        # print(key)
        # print(value)
        # if (len(self.cache)+1)>self.cap:
        #     print(self.last.prev.key)
        #     print(self.cache)
        #     print(self.last.prev.key in self.cache.keys())
        #     # del self.cache[self.last.prev.key]
        #     self.delete(self.last.prev.key)
        # newData = Data(key, value)
        # self.cache[key] = newData
        # self.insert(newData)
        


