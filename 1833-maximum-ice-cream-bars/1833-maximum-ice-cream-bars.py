class Solution(object):
    def maxIceCream(self, costs, coins):
        count = 0
        costs.sort()
        for cost in costs:
            if cost <= coins:
                coins = coins - cost
                count = count + 1
        return count

        