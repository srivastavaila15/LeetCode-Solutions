class Solution(object):
    def removeOuterParentheses(self, s):
        level = 0
        ans = ""
        for i in range(len(s)):
            if s[i] == '(':
                level = level + 1
                if level > 1:
                    ans = ans + s[i]
            else:
                if level > 1:
                    ans = ans + s[i]
                level = level - 1
        return ans
        