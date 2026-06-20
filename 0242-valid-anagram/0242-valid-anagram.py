class Solution(object):
    def isAnagram(self, s, t):
        new_s = "".join(sorted(s))
        new_t = "".join(sorted(t))
        if new_s == new_t:
            return True
        return False
        