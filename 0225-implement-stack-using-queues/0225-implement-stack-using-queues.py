class MyStack:

    def __init__(self):
        from collections import deque
        self.dq = deque()


    def push(self, x: int) -> None:
        self.dq.append(x)


    def pop(self) -> int:
        return self.dq.pop()
        

    def top(self) -> int:
        return self.dq[len(self.dq)-1]
        

    def empty(self) -> bool:
        return len(self.dq) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()