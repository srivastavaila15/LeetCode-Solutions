class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        pattern_to_word = {}
        word_to_pattern = {}
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            p_char = pattern[i]
            w_word = words[i]
            if p_char in pattern_to_word and pattern_to_word[p_char] != w_word:
                return False
            elif w_word in word_to_pattern and word_to_pattern[w_word] != p_char:
                return False
            
            pattern_to_word[p_char] = w_word
            word_to_pattern[w_word] = p_char
            
        return True
        


        