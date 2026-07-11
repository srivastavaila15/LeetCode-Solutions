class Solution(object):
    def lengthOfLongestSubstring(self, s):
        freq = {}
        subs = ""
        start = 0
        max_len = 0
        for end, char in enumerate(s):
            if char in freq and freq[char] >= start:
                start = freq[char] + 1
            freq[char] = end
            current_len = end - start + 1
            if current_len> max_len:
                max_len = current_len
                subs = s[start:end + 1]
        return len(subs)
        
            
        