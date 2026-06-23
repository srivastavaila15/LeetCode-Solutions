class Solution(object):
    def containsDuplicate(self, nums):
        newSet = set()
        for num in nums:
            if num not in newSet:
                newSet.add(num)
            else:
                return True
        return False


        
        
            
    
    


            
        
        