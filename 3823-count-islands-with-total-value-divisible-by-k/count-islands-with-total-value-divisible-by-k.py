class Solution:
    def countIslands(self, grid, k):
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    total = 0
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        if 0 <= x < m and 0 <= y < n and grid[x][y]:
                            total += grid[x][y]
                            grid[x][y] = 0
                            stack += [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                    if total % k == 0:
                            count += 1
        return count