class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for char in stones:
            if char in jewels:
                count = count + 1
        return count
        