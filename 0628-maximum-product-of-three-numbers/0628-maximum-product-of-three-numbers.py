class Solution(object):
    def maximumProduct(self, nums):
        first = float('-inf')
        second = float('-inf')
        third = float('-inf')
        min1 = float('inf')
        min2 = float('inf')
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
            
            if min1 > num:
                min2 = min1
                min1 = num
            elif min2 > num:
                min2 = num
        print('first :', first)
        print('second :', second)
        print('third :', third)
            
        return max(first*second*third, min1*min2*first)
            

        