class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.data = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        idx = self._hash(key)
        if key not in self.data[idx]:
            self.data[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        if key in self.data[idx]:
            self.data[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return key in self.data[idx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)