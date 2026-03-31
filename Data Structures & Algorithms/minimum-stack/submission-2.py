class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_value = val
        if len(self.stack) > 0 and self.stack[-1][1] < min_value:
            min_value = self.stack[-1][1]

        self.stack.append((val, min_value))
        

    def pop(self) -> None:
        del self.stack[-1]


    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
