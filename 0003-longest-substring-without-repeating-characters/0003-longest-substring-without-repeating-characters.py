class Solution(object):
    def lengthOfLongestSubstring(self, s):
        map_s = {}
        mx_ws = 0
        i = j = 0
        for j in range(len(s)):
            if s[j] in map_s and map_s[s[j]] >= i:
                i = map_s[s[j]] + 1
            map_s[s[j]] = j
            ws = j - i + 1
            if mx_ws < ws:
                mx_ws = ws
        return mx_ws



        
            
        