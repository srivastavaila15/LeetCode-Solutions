class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        for x in range(len(nums)-2):
            i = x + 1
            j = len(nums) - 1
            while i < j:
                current_sum = nums[i] + nums[j]+ nums[x]
                if current_sum == target:
                    return current_sum
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                if current_sum < target:
                    i = i + 1
                else:
                    j = j - 1
        return closest_sum
                
