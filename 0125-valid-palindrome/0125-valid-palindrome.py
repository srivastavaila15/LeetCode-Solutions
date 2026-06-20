class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        new_s = ""
        rev = ""
        for i in range(len(s)):
            import re
            if re.match(r"[a-z0-9]", s[i]):
                new_s = new_s + s[i]
        x = len(new_s)-1
        while x>=0:
            rev = rev + new_s[x]
            x = x -1
        if rev == new_s:
            return True
        return False
        
    
                
        
        