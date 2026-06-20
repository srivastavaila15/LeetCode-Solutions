class Solution(object):
    import re
    def isPalindrome(self, s):
        s = s.lower()
        i = 0
        j = len(s)-1
        while(i<j):
            if not re.match(r"[a-z0-9]",s[i]):
                i = i+1
            elif not re.match(r"[a-z0-9]",s[j]):
                j = j - 1
            elif s[i] == s[j]:
                i = i+1
                j = j-1
            else:
                return False
        return True

            
    
                
        
        