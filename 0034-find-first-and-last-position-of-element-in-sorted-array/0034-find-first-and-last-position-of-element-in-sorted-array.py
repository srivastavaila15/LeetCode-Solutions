class Solution(object):
    def searchRange(self, nums, target):
        l = 0
        r = len(nums)-1
        if not nums: return [-1, -1]
        res = [-1, -1]

        while l < r:
            m = l + (r - l)/2
            if target > nums[m]:
                l = m + 1
            else:
                r = m

        if nums[l] == target: 
            res[0] = l 
        else: 
            return [-1, -1]

        l = 0
        r = len(nums)-1
        while l < r:
            m = l + (r - l + 1)/2
            if target < nums[m]:
                r = m - 1
            else:
                l = m
        
        if nums[l] == target: 
            res[1] = l
        else: 
            return [-1,-1]
        return res

        