class Solution(object):
    def dailyTemperatures(self, temperatures):
        stack = []
        n = len(temperatures)
        arr = [0] * n
        stack.append(n-1)
        for i in range(n-2, -1, -1):
            while len(stack):
                top = stack[len(stack)-1]
                if temperatures[i] >= temperatures[top]:
                    stack.pop()
                else:
                    arr[i] = top - i
                    break
            stack.append(i)
        return arr
                

        