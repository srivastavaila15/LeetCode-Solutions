class Solution(object):
    def findPairs(self, nums, k):
        nums.sort()
        i = 0
        j = 1
        seen_pair = set()
        
        while j < len(nums):
            diff = abs(nums[i]-nums[j])
            if i==j or diff < k:
                j = j + 1
            elif diff > k:
                i = i + 1
            else:
                seen_pair.add((nums[i], nums[j]))
                i = i + 1
                j = j + 1
        return len(seen_pair)



        