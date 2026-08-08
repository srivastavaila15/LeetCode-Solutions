class Solution(object):
    def findDuplicates(self, nums):
        ans = []
        for num in nums:
            idx = abs(num) - 1

            if nums[idx] < 0:
                ans.append(abs(num))
            else:
                nums[idx] = -nums[idx]
        return ans
        