class Solution:
    def mySqrt(self, x: int) -> int:
        power = 0.5
        res = x ** power
        return int(res)
        
        