class Solution(object):
    def findDuplicates(self, nums):
        freq = {}
        ans = []
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        for num, val in freq.items():
            if val > 1:
                ans.append(num)
        return ans
        