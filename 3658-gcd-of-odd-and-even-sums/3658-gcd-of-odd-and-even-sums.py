class Solution(object):
    def gcdOfOddEvenSums(self, n):
        sumOdd = n * n
        sumEven = n * (n + 1)
        while sumOdd:
            sumEven, sumOdd = sumOdd, sumEven % sumOdd
        return sumEven
        