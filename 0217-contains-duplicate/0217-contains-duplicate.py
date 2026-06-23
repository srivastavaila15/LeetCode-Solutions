class Solution(object):
    def containsDuplicate(self, nums):
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] = freq[nums[i]] + 1
        for key, count in freq.items():
            if count >= 2:
                return True
        return False
        
        
            
    
    


            
        
        