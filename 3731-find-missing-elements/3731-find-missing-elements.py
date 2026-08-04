class Solution(object):
    def findMissingElements(self, nums):
        ans = set(nums)
        max_num = max(nums)
        min_num = min(nums)
        curr = min_num
        new_nums = []
        while curr <= max_num:
            if curr not in ans:
                new_nums.append(curr)
            curr = curr + 1
        return new_nums
            

        
        