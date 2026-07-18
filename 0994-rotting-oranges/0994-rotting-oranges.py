class Solution(object):
    def orangesRotting(self, grid):
        m = len(grid)
        n = len(grid[0])
        #queue = []
        queue = deque()
        maxlvl = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i,j,0])
        
        while len(queue):
            [x, y, lvl] = queue.popleft()
            maxlvl = max(lvl, maxlvl)
            if x>0 and grid[x-1][y] == 1:
                grid[x-1][y] = 2
                queue.append([x-1, y, lvl+1])
            if x< m-1 and grid[x+1][y] == 1:
                grid[x+1][y] = 2
                queue.append([x+1, y, lvl+1])
            if y >0 and grid[x][y-1] == 1:
                grid[x][y-1] = 2
                queue.append([x, y-1, lvl+1])
            if y < n-1 and grid[x][y+1] == 1:
                grid[x][y+1] = 2
                queue.append([x, y+1, lvl+1])


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
            
        return maxlvl
