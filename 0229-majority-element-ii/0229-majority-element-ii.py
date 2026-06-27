class Solution(object):
    def majorityElement(self, nums):
        n = len(nums) // 3
        freq = {}
        result = []
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] = freq[nums[i]] + 1
        
        for val, count in freq.items():
            if count > n and val not in result:
                result.append(val)
        return result
        