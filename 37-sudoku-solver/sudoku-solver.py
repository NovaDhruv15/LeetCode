class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for r in range(9):
            for c in range(9):
                d = board[r][c]
                if d == ".":
                    empty.append((r, c))
                else:
                    b = (r // 3) * 3 + c // 3
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[b].add(d)

        def solve(pos):
            if pos == len(empty):
                return True

            best = pos
            best_choices = None

            for i in range(pos, len(empty)):
                r, c = empty[i]
                b = (r // 3) * 3 + c // 3
                choices = set("123456789") - rows[r] - cols[c] - boxes[b]

                if best_choices is None or len(choices) < len(best_choices):
                    best, best_choices = i, choices
                if not best_choices:
                    return False

            empty[pos], empty[best] = empty[best], empty[pos]
            r, c = empty[pos]
            b = (r // 3) * 3 + c // 3

            for d in best_choices:
                board[r][c] = d
                rows[r].add(d)
                cols[c].add(d)
                boxes[b].add(d)

                if solve(pos + 1):
                    return True

                board[r][c] = "."
                rows[r].remove(d)
                cols[c].remove(d)
                boxes[b].remove(d)

            empty[pos], empty[best] = empty[best], empty[pos]
            return False

        solve(0)