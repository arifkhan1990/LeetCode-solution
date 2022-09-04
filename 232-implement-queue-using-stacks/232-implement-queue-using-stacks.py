class MyQueue:

    def __init__(self):
        self.front = []
        self.back = []
        self.top = None

    def push(self, x: int) -> None:
        if not self.front:
            self.top = x
        self.front.append(x)
        

    def pop(self) -> int:
        if not self.back:
            while self.front:
                self.back.append(self.front.pop())
        return self.back.pop()
        

    def peek(self) -> int:
        if self.back:
            return self.back[-1]
        return self.top

    def empty(self) -> bool:
        return not self.front and not self.back


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()