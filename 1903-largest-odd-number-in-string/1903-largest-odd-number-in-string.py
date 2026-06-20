class Solution(object):
    def largestOddNumber(self, num):
        num = int(num)
        while(num>=1):
            if num%2 != 0:
                return str(num)
            else:
                num = num//10
                #num = num - 1
        return ""
            



        