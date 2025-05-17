class Solution:
    def numIslands(self, grid):
        def fire(m, i, j):
            if i < 0 or i >= len(m) or j < 0 or j >= len(m[0]) or m[i][j] != '1':
                return
            m[i][j] = '2'
            fire(m, i+1, j)
            fire(m, i-1, j)
            fire(m, i, j+1)
            fire(m, i, j-1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    fire(grid, i, j)
                    count += 1
        return count