class Solution(object):
    def isPerfectSquare(self, num):
        power = 0.5
        sqrt = num ** power
        if sqrt%1 == 0:
            return True
        return False
        
        

        