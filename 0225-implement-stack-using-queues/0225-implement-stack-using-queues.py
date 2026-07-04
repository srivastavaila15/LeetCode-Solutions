class MyStack(object):

    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.q1 = deque([])
        self.q2 = deque([])
        temp = []
        

    def push(self, x):
        self.q1.append(x)
        

    def pop(self):
        n = (self.q1)
        for i in range(len(n)-1):
            firstEle = self.q1.popleft()
            self.q2.append(firstEle)
        
        popEle = self.q1.popleft()
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp
        return popEle

        

    def top(self):
        n = (self.q1)
        for i in range(len(n) - 1):
            firstEle = self.q1.popleft()
            self.q2.append(firstEle)
        
        topEle = self.q1.popleft()
        self.q2.append(topEle)

        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

        return topEle
        

    def empty(self):
        #n = len(q1)
        if len(self.q1) == 0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()