# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        l = 1
        r = n
        while l < r:
            m = l + (r - l)/2
            if not isBadVersion(m):
                l = m + 1
            else:
                r = m
        return l

            
        