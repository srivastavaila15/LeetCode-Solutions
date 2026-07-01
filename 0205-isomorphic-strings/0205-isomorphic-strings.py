class Solution(object):
    def isIsomorphic(self, s, t):
        map_s_t = {}
        map_t_s = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in map_s_t and map_s_t[s[i]] != t[i]:
                return False

            elif t[i] in map_t_s and map_t_s[t[i]] != s[i]:
                return False
            map_t_s[t[i]] = s[i]
            map_s_t[s[i]] = t[i]
        
        
        return True
            
            


        