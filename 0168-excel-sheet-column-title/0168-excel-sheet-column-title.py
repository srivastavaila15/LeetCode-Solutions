class Solution(object):
    def convertToTitle(self, columnNumber):
        res = ""
        while columnNumber > 0:
            columnNumber = columnNumber - 1
            rem = columnNumber % 26
            print(chr(rem+ 65))
            res = res + chr(rem + 65)
            columnNumber = columnNumber // 26
        return res[::-1]


        
        