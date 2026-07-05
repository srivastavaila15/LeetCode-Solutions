class Solution(object):
    def removeOuterParentheses(self, s):
        stack = []
        ans = ""
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                if len(stack) > 1:
                    ans = ans + s[i]
            else:
                if len(stack) > 1:
                    ans = ans + s[i]
                stack.pop()
        return ans
        