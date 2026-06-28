class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result = result ^ i 
        return result



            
        