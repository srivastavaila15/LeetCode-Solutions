class Solution(object):
    def findDuplicate(self, nums):
        newSet = set()
        for num in nums:
            if num not in newSet:
                newSet.add(num)
            else:
                return num
        