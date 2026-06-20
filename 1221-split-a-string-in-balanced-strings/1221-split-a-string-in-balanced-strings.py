class Solution(object):
    def balancedStringSplit(self, s):
        temp = 0
        count = 0
        for char in s:
            if char == 'R':
                temp = temp + 1
            else:
                temp = temp -1
            if temp == 0:
                count = count + 1
        return count


        
        
        