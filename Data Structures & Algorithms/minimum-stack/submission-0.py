class MinStack:

    def __init__(self):
        self.stack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        return None

    def pop(self) -> None:
        if self.stack:
            self.stack.pop(-1)
        return None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None
    
    def getMin(self) -> int:
        if self.stack:
            return min(self.stack)
        return None
        
