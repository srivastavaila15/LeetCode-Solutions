class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        left = 2
        right = x/2
        while left <= right:
            mid = (left + right)/2
            if x == mid**2:
                return mid
            elif mid**2 < x:
                left = mid + 1
            else:
                right = mid -1
        return right
        