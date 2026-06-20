class Solution(object):
    def countSegments(self, s):
        count = 0
        res = []
        for i in range(len(s)):
            if s[i]!= " ":
                if i == 0 or s[i-1] == " ":
                    count = count + 1
        return count

            
        
        