class MyStack(object):

    def __init__(self):
        self.q1 = []
        self.q1 = deque([])

    def push(self, x):
        self.q1.append(x)
        

    def pop(self):
        n = len(self.q1)
        for i in range(n-1):
            self.q1.append(self.q1.popleft())
        return self.q1.popleft()
        

    def top(self):
        n = len(self.q1)
        for i in range(n-1):
            self.q1.append(self.q1.popleft())
        topEle = self.q1.popleft()
        self.q1.append(topEle)
        return topEle
        

    def empty(self):
        if len(self.q1) == 0:
            return True
        return False
        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()