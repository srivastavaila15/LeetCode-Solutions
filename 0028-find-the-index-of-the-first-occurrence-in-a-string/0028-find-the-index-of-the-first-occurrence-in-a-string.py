class Solution(object):
    def strStr(self, haystack, needle):
        i = 0
        j = 1
        h = len(haystack)
        n = len(needle)
        lps = [0] * n
        while j < n:
            if needle[i] == needle[j]:
                lps[j] = i + 1
                i = i+1
                j = j+1
            else:
                if i == 0:
                    lps[j] = 0
                    j = j+1
                else:
                    i = lps[i-1]
        i = 0 
        j = 0
        while(i < h):
            if haystack[i] == needle[j]:
                i = i+1
                j = j+1
            else:
                if j == 0:
                    i = i+1
                else:
                    j = lps[j-1]
            if j == n:
                return i - n
        return -1 

