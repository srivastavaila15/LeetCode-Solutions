class Solution(object):
    def intersect(self, nums1, nums2):
        nums1 = sorted(nums1)  
        nums2 = sorted(nums2)
        i = 0
        j = 0
        res = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                #res.append(nums2[j])    
                i = i+1
                j = j+1
            elif nums1[i] < nums2[j]:
                i = i + 1
            else:
                j = j+1
        return res

        
        
        
       
        
        
        

        

        