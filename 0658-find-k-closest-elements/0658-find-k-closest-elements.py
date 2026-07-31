class Solution(object):
    def findClosestElements(self, arr, k, x):
        subarr = []
        l = 0
        r = len(arr) - 1
        while l < r:
            m = l + (r - l)//2
            if m + k < len(arr) and (arr[m+k]-x) < (x - arr[m]):
                l = m + 1
            else:
                r = m
        return arr[l : l + k]
        