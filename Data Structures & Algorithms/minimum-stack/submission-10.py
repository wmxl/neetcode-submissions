class MinStack:

    def __init__(self):
        self.stack = []
        self.mi = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1:
            self.mi.append(val) 
        else:
            if val < self.getMin():
                self.mi.append(val)
            else:
                self.mi.append(self.getMin())
        

    def pop(self) -> None:
        self.mi.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.mi:
            return None
        return self.mi[-1]

        
