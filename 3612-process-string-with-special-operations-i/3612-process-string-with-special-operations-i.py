class Solution(object):
    def processStr(self, s):
        newS = ""
        for char in s:
            if char == '#':
                newS = newS + newS
            elif char == '%':
                newS = newS[::-1]
            elif char == '*':
                newS = newS[:-1]
            else:
                newS = newS + char
        return newS
        