class Solution(object):
    def getMinDistance(self, nums, target, start):
        min_dist = float('inf')
        for i in range(len(nums)):
            if target == nums[i]:
                dist = abs(i - start)
            
                if dist < min_dist:
                    min_dist = dist
            
                if min_dist == 0:
                    return 0
            
        return min_dist if min_dist != float('inf') else -1


        