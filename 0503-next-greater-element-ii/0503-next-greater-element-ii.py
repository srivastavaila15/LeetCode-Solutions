class Solution(object):
    def nextGreaterElements(self, nums):
        double_nums = nums * 2
        stack = []
        n = len(double_nums)
        arr = [-1] * n
        stack.append(double_nums[-1])
        top = stack[-1]
        for i in range(n-2, -1, -1):
            while len(stack):
                top = stack[len(stack)-1]
                if double_nums[i] >= top:
                    stack.pop()
                else:
                    arr[i] = top
                    break
            stack.append(double_nums[i])
        return arr[0:n//2]
            
        