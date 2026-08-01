class Solution(object):
    def twoSum(self, nums, target):
        pair_map = {}
        for i in range(0, len(nums)):
            if nums[i] not in pair_map:
                pair_map[nums[i]] = i
        
        for j in range(0, len(nums)):
            pair_val = target - nums[j]
            if pair_val in pair_map and pair_map[pair_val] != j:
                return [j, pair_map[pair_val]]
        
        