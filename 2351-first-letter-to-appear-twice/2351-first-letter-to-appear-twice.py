class Solution(object):
    def repeatedCharacter(self, s):
        newS = set()
        seen = 0
        for char in s:
            if char not in newS:
                newS.add(char)
            else:
                return char
        
            

            
        