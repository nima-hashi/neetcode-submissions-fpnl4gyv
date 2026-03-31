class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subBox = {}

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                # Check row
                if val in rows[i]:
                    return False
                rows[i].add(val)

                # Check column
                if val in cols[j]:
                    return False
                cols[j].add(val)

                # Check sub-box
                box_key = (i // 3, j // 3)
                if box_key not in subBox:
                    subBox[box_key] = set()
                if val in subBox[box_key]:
                    return False
                subBox[box_key].add(val)

        return True