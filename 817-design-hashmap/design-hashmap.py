class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.data = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        for i, (k, _) in enumerate(self.data[idx]):
            if k == key:
                self.data[idx][i] = (key, value)
                return
        self.data[idx].append((key, value))
        
    def get(self, key: int) -> int:
        idx = self._hash(key)
        for k, v in self.data[idx]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        for i, (k, _) in enumerate(self.data[idx]):
            if k == key:
                del self.data[idx][i]
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)