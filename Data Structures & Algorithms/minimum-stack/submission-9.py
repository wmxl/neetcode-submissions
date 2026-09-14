class MinStack:

    def __init__(self):
        self.stack = []
        self.mi = None
        

    def push(self, val: int) -> None:
        if self.mi == None:
            self.mi = val
        if val < self.mi:
            self.mi = val
        self.stack.append(val)
        

    def pop(self) -> None:
        # print('pop')
        # print(self.stack)
        if not self.stack:
            return None
        pop = self.stack.pop()
        # print(pop)
        if self.stack:
            self.mi = self.stack[0]
            for i in self.stack:
                self.mi = min(self.mi, i)
        else:
            self.mi = None
        # print(self.stack)
        # print(self.top())
        return pop
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mi

        
