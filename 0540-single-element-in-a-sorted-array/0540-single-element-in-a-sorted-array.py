class Solution(object):
    def singleNonDuplicate(self, nums):
        l = 0
        r = len(nums)-1
        while l <= r:
            m = l + (r - l)//2
            if m > 0 and nums[m] == nums[m-1]:
                leftcount = (m-1) - l
                if leftcount % 2 == 1:
                    r = m - 2
                else:
                    l = m + 1
            elif m < len(nums)-1 and nums[m] == nums[m + 1]:
                leftcount = m - l
                if leftcount % 2 == 1:
                    r = m - 1
                else:
                    l = m + 2
            else:
                return nums[m]
        


        
        