class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        ans = []
        seen = set()
        row = len(grid)
        col = len(grid[0])
        total_sum = row*col*(row*col + 1)//2
        for i in range(row):
            for j in range(col):
                if grid[i][j] not in seen:
                    seen.add(grid[i][j])
                else:
                    ans.append(grid[i][j])
        seen_sum = sum(seen)
        res = total_sum - seen_sum
        ans.append(res)
        return ans
        