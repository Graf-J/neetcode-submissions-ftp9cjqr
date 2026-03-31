class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        prev_min = float('inf') if not self.stack else self.stack[-1][1]
        self.stack.append((val, min(val, prev_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

