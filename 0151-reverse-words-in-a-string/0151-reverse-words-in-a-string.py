class Solution(object):
    def reverseWords(self, s):
        new_s = ""
        words = s.split()
        for word in reversed(words):
            print(word)
            new_s = new_s +" "+ word
        new_s = new_s.lstrip()
        return new_s
        