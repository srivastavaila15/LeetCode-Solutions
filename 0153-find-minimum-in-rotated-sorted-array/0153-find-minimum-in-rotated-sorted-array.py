class Solution(object):
    def findMin(self, nums):
        l = 0
        r = len(nums)-1
        while l <= r:
            m = l + (r-l)/2
            if nums[l] <= nums[r]:
                return nums[l]
            if nums[m] < nums[m-1]:
                return nums[m]
            if nums[l] > nums[m]:
                r = m - 1
            else:
                l = m + 1
        return l

        