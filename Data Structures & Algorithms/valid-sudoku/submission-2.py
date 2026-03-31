class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [[] for i in range(len(board))] 
        cols = [[] for i in range(len(board))]
        subBox = {}


        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j]:
                    return False
                rows[i].append(board[i][j])
                cols[j].append(board[i][j])
                if (i//3, j//3) not in subBox:
                    subBox[(i//3, j//3)] = [board[i][j]]
                else:
                    if board[i][j] in subBox[(i//3, j//3)]:
                        return False
                    subBox[(i//3, j//3)].append(board[i][j])
                    
        return True
                


        