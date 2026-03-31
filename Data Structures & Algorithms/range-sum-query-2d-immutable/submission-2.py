class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        m, n = len(matrix), len(matrix[0])

        for x in range(m):
            for y in range(n):
                # keeping track of what to add
                top = matrix[x-1][y] if x > 0 else 0
                # keeping track of what to add
                left = matrix[x][y-1] if y > 0 else 0  
                #check if top left corner exists
                topLeft = matrix[x-1][y-1] if (x > 0 and y > 0) else 0
                
                matrix[x][y] += top + left - topLeft
        
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        top = self.matrix[row1-1][col2] if (row1-1 >= 0) else 0
        left = self.matrix[row2][col1-1] if (col1-1 >= 0) else 0
        topLeft = self.matrix[row1-1][col1-1] if (row1-1 >= 0 and col1-1 >= 0) else 0

        return self.matrix[row2][col2] - top - left + topLeft



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)