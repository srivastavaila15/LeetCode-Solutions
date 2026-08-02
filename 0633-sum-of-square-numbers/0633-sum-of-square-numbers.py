class Solution(object):
    def judgeSquareSum(self, c):
        import math
        l = 0
        r = int(math.sqrt(c))
        while l <= r:
            if (l*l + r*r) == c:
                return True
            elif (l*l + r*r) > c:
                r = r - 1
            else:
                l = l + 1
        return False
        