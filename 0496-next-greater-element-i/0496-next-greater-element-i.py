class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        mapEle = {}
        stack.append(nums2[-1])
        top = stack[-1]
        n = len(nums2)
        arr = []
        mapEle = {nums2[-1]:-1}
        for i in range(n-1, -1, -1):
            while len(stack):
                top = stack[len(stack)-1]
                if nums2[i] < top:
                    mapEle[nums2[i]] = stack[len(stack)-1]
                    break
                else:
                    stack.pop()
            if not len(stack):
                mapEle[nums2[i]] = -1
            stack.append(nums2[i])

        for j in range(len(nums1)):
            arr.append(mapEle.get(nums1[j], -1))
        return arr
        

        

        