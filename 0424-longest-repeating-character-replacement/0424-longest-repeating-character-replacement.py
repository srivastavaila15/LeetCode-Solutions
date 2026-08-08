class Solution(object):
    def characterReplacement(self, s, k): 
        if not s:
            return 0
        validMap = {}
        i = j = 0
        validMap[s[0]] = 1
        maxWindowLen = 0
        while j < len(s):
            if self.isWindowValid(validMap, k):
                maxWindowLen = max(maxWindowLen, j-i+1)
                j += 1
                if j < len(s):
                    validMap[s[j]] = validMap.get(s[j], 0) + 1
            else:
                validMap[s[i]] -= 1
                i += 1
        return maxWindowLen
            
        
    def isWindowValid(self, validMap, k):
        totalCount = 0
        maxCount = 0
        for i in range(26):
            char = chr(i + 65)
            if char in validMap and validMap[char] > 0:
                totalCount += validMap[char]
                maxCount = max(maxCount, validMap[char])
        return (totalCount - maxCount) <= k
            

    
            

        