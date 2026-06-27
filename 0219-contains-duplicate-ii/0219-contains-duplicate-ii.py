class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        freq = {}
        for i, num in enumerate(nums):
            if num in freq:
                if i - freq[num] <= k:
                    return True
            freq[num] = i
        return False



        