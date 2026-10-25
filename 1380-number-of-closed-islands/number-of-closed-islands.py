class Solution:
    def closedIsland(self, grid):
        R, C = len(grid), len(grid[0])

        def sink(r, c):
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] == 1:
                return
            grid[r][c] = 1
            sink(r + 1, c)
            sink(r - 1, c)
            sink(r, c + 1)
            sink(r, c - 1)

        for r in range(R):
            for c in range(C):
                if r in (0, R - 1) or c in (0, C - 1):
                    sink(r, c)

        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    count += 1
                    sink(r, c)
        return count