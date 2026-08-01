class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for x in range(len(nums)-2):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            self.twoSum(nums, x, ans)
        return ans
        
    
    def twoSum(self, nums, x, ans):
        i = x + 1
        j = len(nums)-1
        while i < j:
            sum_target = nums[i] + nums[j] + nums[x]
            if sum_target > 0:
                j = j - 1
            elif sum_target < 0:
                i = i + 1
            else:
                ans.append([nums[i], nums[j], nums[x]])
                i = i+1
                j = j-1
                while i<j and nums[i] == nums[i -1]:
                    i = i+1
