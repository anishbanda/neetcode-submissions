class MinStack:

    def __init__(self):
        self.stack = []
        self.small = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.small = val
        else:
            self.stack.append(val - self.small)
            if val < self.small:
                self.small = val

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop = self.stack.pop()

        if pop < 0:
            self.small = self.small - pop


    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.small
        else:
            return self.small

    def getMin(self) -> int:
        return self.small
