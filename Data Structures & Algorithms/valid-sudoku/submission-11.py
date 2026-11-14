class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        squares = {i:[] for i in range(9)}
        rows = {i:[] for i in range(9)}
        cols = {i:[] for i in range(9)}

        for i in range(9):
            for j in range(9):
                elm = board[i][j]
                if elm.isdigit():
                    square = (i // 3) * 3 + (j // 3)
                    if (elm in rows[i]) or (elm in cols[j]) or (elm in squares[square]):
                        return False
                    rows[i].append(elm)
                    cols[j].append(elm)
                    squares[square].append(elm)
        
        return True

        