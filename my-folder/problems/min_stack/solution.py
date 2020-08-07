class MinStack:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        return
        
    def push(self, x: int) -> None:
        self.stack_1.append(x)
        if len(self.stack_2)==0:
            self.stack_2.append(x)
        else:
            if x <= self.stack_2[-1]:
                self.stack_2.append(x)
        return

    def pop(self) -> None:
        if self.stack_1[-1] == self.stack_2[-1]:
            self.stack_2.pop()
        self.stack_1.pop()
        return

    def top(self) -> int:
        if(len(self.stack_1) != 0):
            return self.stack_1[-1]
        else:
            return 0

    def getMin(self) -> int:
        if len(self.stack_2)!=0:
            return self.stack_2[-1]
        else:
            return 0
        
  