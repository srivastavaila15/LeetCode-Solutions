class Solution(object):
    def isPalindrome(self, x):
        temp = 0
        y = 0
        digit = x
        while digit>0:
            temp = digit%10
            digit = digit//10
            y = (y * 10) + temp
            print(y)
            
        if x == y:
            return True
        return False
        

        