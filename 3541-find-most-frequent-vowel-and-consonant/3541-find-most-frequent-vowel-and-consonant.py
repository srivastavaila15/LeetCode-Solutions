class Solution(object):
    def maxFreqSum(self, s):
        freq = {}
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]] = freq[s[i]] + 1
        vowel = ['a', 'e', 'i', 'o', 'u']
        mx_vowel = mx_const = 0
        for char, count in freq.items():
            if char in vowel:
                mx_vowel = max(mx_vowel, count)
            else:
                mx_const = max(mx_const, count)
        return (mx_vowel + mx_const)
