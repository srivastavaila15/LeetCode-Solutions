class Solution(object):
    def duplicateNumbersXOR(self, nums):
        freq = {}
        result = 0
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] = freq[nums[i]] + 1
        for i, count in freq.items():
            if count == 2:
                result = result ^ i
        return result
        