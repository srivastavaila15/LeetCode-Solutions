class MinStack(object):

    def __init__(self):
        self.s1 = []
        

    def push(self, value):
        if len(self.s1) == 0:
            self.s1.append([value, value])
        else:
            current_min = self.s1[-1][1]
            if value < current_min:
                new_min = value
            else:
                new_min = current_min
            self.s1.append([value, new_min])
        

    def pop(self):
        self.s1.pop()
        

    def top(self):
            return self.s1[len(self.s1)-1][0]
        

    def getMin(self):
        return self.s1[len(self.s1)-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()