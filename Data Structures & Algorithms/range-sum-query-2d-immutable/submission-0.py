class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        #self.matrix = matrix
        
        self.numMat = [[0] * (COLS+1) for i in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                self.numMat[r + 1][c + 1] = prefix + self.numMat[r][c+1]
        print(self.numMat)

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        full = self.numMat[row2 + 1][col2 + 1]
        left = self.numMat[row2+1][col1]
        top = self.numMat[row1][col2 + 1]
        corner = self.numMat[row1][col1]

        return full - left - top + corner
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

[
    [[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], 
    [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]
]