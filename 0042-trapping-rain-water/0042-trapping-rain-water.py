class Solution(object):
    def trap(self, height):
        if not height:
            return 0

        n = len(height)
        maxL = [0]*n
        maxL[0] = height[0]
        sum_height = 0
        for i in range(1, n):
            maxL[i] = max(maxL[i-1], height[i])

        maxR = [0]*n
        maxR[-1] = height[-1]
        for j in range(n-2, -1, -1):
            maxR[j] = max(maxR[j+1], height[j])
        for x in range(len(height)):
            curr_height = min(maxL[x], maxR[x]) - height[x]
            sum_height = sum_height + curr_height
        return sum_height

        
        
        