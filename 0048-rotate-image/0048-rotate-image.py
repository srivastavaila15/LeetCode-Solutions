class Solution(object):
    def rotate(self, grid):
        m = len(grid)

        for i in range(m):
            for j in range(i+1, m):
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
            
        for i in range(m):
            grid[i].reverse()
        
        return grid