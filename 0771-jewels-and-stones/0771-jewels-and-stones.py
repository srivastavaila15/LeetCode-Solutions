class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jSet = set()
        for i in range(len(jewels)):
            jSet.add(jewels[i])
        count = 0
        for i in range(len(stones)):
            if stones[i] in jSet:
                count = count + 1
        return count

        