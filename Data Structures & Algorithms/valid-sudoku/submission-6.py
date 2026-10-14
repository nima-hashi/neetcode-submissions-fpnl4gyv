class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                square_row = i // 3
                square_col = j // 3

                if (num in rows[i] or
                    num in cols[j] or
                    num in squares[square_row][square_col]):
                    return False

                rows[i].add(num)
                cols[j].add(num)
                squares[square_row][square_col].add(num)

        return True

        