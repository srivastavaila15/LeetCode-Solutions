class Solution(object):
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        k = k % (m * n)
        while k:
            prev = grid[m - 1][n - 1]
            for i in range(m):
                for j in range(n):
                    grid[i][j], prev = prev, grid[i][j]
            k = k - 1
        return grid
        