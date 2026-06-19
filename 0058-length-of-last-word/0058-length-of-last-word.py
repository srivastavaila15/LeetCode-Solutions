class Solution(object):
    def lengthOfLastWord(self, s):
        n = len(s) -1
        count = 0
        while(n>=0):
            if(s[n] == " "):
                n -=1
            else:
                break
        while(n>=0):
            if(s[n] != " "):
                n -=1
                count +=1
            else:
                break
        return count

        