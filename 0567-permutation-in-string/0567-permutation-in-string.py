class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        hashW = [0]*26
        hashP = [0]*26
        windowLength = len(s1)
        for i in range(windowLength):
            hashP[ord(s1[i]) - 97] += 1
            hashW[ord(s2[i]) - 97] += 1
        i = 0
        j = windowLength - 1
        while j < len(s2):
            if self.isHashMatching(hashW, hashP):
                return True
            else:                
                hashW[ord(s2[i]) -97] -= 1
                i = i + 1
                j = j + 1
                if j < len(s2):
                    hashW[ord(s2[j]) - 97] += 1
        return False

    def isHashMatching(self, hashW, hashP):
        for i in range(26):
            if hashW[i] != hashP[i]:
                return False
        return True

        
        
        