class Solution(object):
    def smallestNumber(self, n, t):
         
        curr = n
        while True:
            mul = 1
            temp = curr
            while temp > 0:
                rem = temp % 10
                mul = mul * rem
                temp = temp // 10
            
            if mul % t == 0:
                return curr
            curr = curr + 1
            
            
            
        
        
        