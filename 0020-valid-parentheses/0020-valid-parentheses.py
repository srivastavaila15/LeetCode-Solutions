class Solution(object):
    def isValid(self, s):
        stack = []
        my_map = {'(':')', '{':'}' , '[':']'}
        for i in range(len(s)):
            if s[i] in my_map:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                top = stack.pop()
                if not top or s[i] != my_map[top]:
                    return False
        return len(stack) == 0