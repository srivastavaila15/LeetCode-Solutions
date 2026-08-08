class Solution(object):
    def thirdMax(self, nums):
        ele1 = float('-inf')
        ele2 = float('-inf')
        ele3 = float('-inf')
        for num in nums:
            if num == ele1 or num == ele2 or num == ele3:
                continue
            if num > ele1:
                ele3 = ele2
                ele2 = ele1
                ele1 = num
            elif num > ele2:
                ele3 = ele2
                ele2 = num
            elif num > ele3:
                ele3 = num
        return ele3 if ele3 != float('-inf') else ele1


                

        