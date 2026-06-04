class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0 or self.stack[-1][1] > val:
            min_val = val
        else:
            min_val = self.stack[-1][1]

        self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
