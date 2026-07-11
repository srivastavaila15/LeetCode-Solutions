class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        res = ""
        #if len(num) == k: return "0"
        #stack.append(num[0])
        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k = k - 1
            stack.append(digit)
        if k > 0:
            stack = stack[:-k]
        res = "".join(stack).lstrip('0')
        return res if res else "0"
            
            
        