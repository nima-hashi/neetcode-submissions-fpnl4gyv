class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validRow = {i:set() for i in range(9)}
        validCol = {i: set() for i in range(9)}
        subBox = {i: set() for i in range(9)}

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                boxId = (i // 3) * 3 + (j // 3)
                if (val in validRow[i]) or (val in validCol[j]) or (val in subBox[boxId]):
                    return False
                
                validRow[i].add(val)
                validCol[j].add(val)
                subBox[boxId].add(val)
        return True

        