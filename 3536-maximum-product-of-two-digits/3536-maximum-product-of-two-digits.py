class Solution(object):
    def maxProduct(self, n):
        digits = [int(d) for d in str(n)]
        max1 = max2 = float('-inf')
    
        for num in digits:
            if num > max1:
                max2 = max1  # Shift previous largest to 2nd largest
                max1 = num   # Set new largest
            elif num > max2: # Runs ONLY if num wasn't larger than max1
                max2 = num
            
        print(max1, max2)   
            # if num < min1:
            #     min2 = min1
            #     min1 = num
            # else:
            #     min2 = num
        return (max1 * max2)
        