class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        start = (0, 0, grid[0][0])
        stack = [start]
        seen = {start}
        best = 1024

        while stack:
            row, col, val = stack.pop()

            if row == rows - 1 and col == cols - 1:
                best = min(best, val)

            if row + 1 < rows:
                down = (row + 1, col, val ^ grid[row + 1][col])
                if down not in seen:
                    seen.add(down)
                    stack.append(down)

            if col + 1 < cols:
                right = (row, col + 1, val ^ grid[row][col + 1])
                if right not in seen:
                    seen.add(right)
                    stack.append(right)

        return best