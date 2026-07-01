class Solution(object):
    def longestCommonPrefix(self, strs):
        x = 0
        while x < len(strs[0]):
            ch = strs[0][x]
            for i in range(len(strs)):
                if x == len(strs[i]) or ch != strs[i][x]:
                    return strs[0][:x]
            x = x + 1
        return strs[0]
            
        
        