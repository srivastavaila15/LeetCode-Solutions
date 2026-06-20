class Solution(object):
    def balancedStringSplit(self, s):
        r_count = 0
        l_count = 0
        count = 0
        for char in s:
            if char == 'R':
                r_count = r_count + 1
            else:
                l_count = l_count + 1
            if r_count == l_count:
                count = count + 1
                r_count = l_count = 0
        return count


        
        
        