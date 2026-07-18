class Solution(object):
    def findGCD(self, nums):
        n = len(nums)
        mn = nums[0]
        mx = nums[0]
        for i in range(n):
            if nums[i] > mx:
                mx = nums[i]
            if nums[i] < mn:
                mn = nums[i]
        a, b = mn, mx
        while b:
            a, b = b, a% b
        return a

        