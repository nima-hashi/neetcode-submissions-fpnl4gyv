from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        found = False

        def backtrack(r, c, index):
            nonlocal found
            if found:
                return

            if goal_reached(index):
                found = True
                return

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not should_skip(nr, nc, index):
                    char = board[nr][nc]
                    board[nr][nc] = "#"  # mark visited
                    backtrack(nr, nc, index + 1)
                    board[nr][nc] = char  # unmark

        def goal_reached(index):
            return index == len(word)

        def should_skip(r, c, index):
            # Out of bounds or mismatch or visited
            return (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] != word[index]
            )

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    board[r][c] = "#"  # mark visited
                    backtrack(r, c, 1)
                    board[r][c] = word[0]
                    if found:
                        return True

        return False
