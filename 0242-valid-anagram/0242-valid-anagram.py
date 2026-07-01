class Solution(object):
    def isAnagram(self, s, t):
        s_map = {}
        t_map = {}
        for ch in s:
            if ch not in s_map:
                s_map[ch] = 1
            else:
                s_map[ch] = s_map[ch] + 1
        for ch in t:
            if ch not in t_map:
                t_map[ch] = 1
            else:
                t_map[ch] = t_map[ch] + 1
        if s_map == t_map:
            return True
        return False

        