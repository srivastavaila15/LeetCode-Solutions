class Solution(object):
    def addDigits(self, num):
        while num >=10:
            add_num = 0
            while num > 0:
                rem = num%10
                add_num = add_num + rem
                num = num //10
            num = add_num
        return num
        
            

        