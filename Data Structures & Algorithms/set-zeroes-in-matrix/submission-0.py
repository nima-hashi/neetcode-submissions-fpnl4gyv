class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        rowZero, colZero = False, False

        # check if first row is to be zero'd
        if 0 in matrix[0]:
            rowZero = True

        # check if first col is to be zero'd
        for i in range(m):
            if matrix[i][0] == 0:
                colZero = True
        
        # loop through rest of matrix and set the col,row to 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # loop through first row and mark row 0
        for i in range(1,m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0


        # loop through first col and mark row 0
        for i in range(1,n):
            if matrix[0][i] == 0:
                for j in range(m):
                    matrix[j][i] = 0

        # mark first row 0 if rowZero
        if rowZero:
            for i in range(n):
                matrix[0][i] = 0


        # mark first col 0 if colZero
        if colZero:
            for i in range(m):
                matrix[i][0] = 0


        





        


        



        
        