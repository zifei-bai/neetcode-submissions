class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.prefix:
            self.prefix.append(val)
        else:
            self.prefix.append(min(self.prefix[-1], val))

    def pop(self) -> None:
        popped = self.stack.pop()
        self.prefix.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix[-1]
