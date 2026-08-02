class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        ans = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                self.twoSum(nums, i, j, target, ans)
        return ans
    
    def twoSum(self, nums, x, y, target, ans):
        i = y + 1
        j = len(nums)-1
        while i < j:
            current_sum = nums[i] + nums[j] + nums[x] + nums[y]
            if current_sum > target:
                j = j -1
            elif current_sum < target:
                i = i + 1
            else:
                ans.append([nums[x], nums[y], nums[i], nums[j]])
                i = i + 1
                j = j - 1
                while i < j and nums[i] == nums[i - 1]:
                    i = i + 1