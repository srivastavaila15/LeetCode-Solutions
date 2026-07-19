class Solution(object):
    def peakIndexInMountainArray(self, arr):
        l = 0
        r = len(arr)-1
        while l < r:
            m = l + (r - l)/2
            if arr[m] > arr[m+1]:
                r = m
            else:
                l = m + 1
        return l

        