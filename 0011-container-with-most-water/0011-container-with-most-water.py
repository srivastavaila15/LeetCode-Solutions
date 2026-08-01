class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        curr_area = float('-inf')
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if curr_area < area:
                curr_area = area
            if height[i] > height[j]:
                j = j-1
            else:
                i = i + 1
        return curr_area
        