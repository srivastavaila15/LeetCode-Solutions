class Solution(object):
    def getCommon(self, nums1, nums2):
        res = list(set(nums1) & set(nums2))
        return -1 if not res else min(res) 
            
        