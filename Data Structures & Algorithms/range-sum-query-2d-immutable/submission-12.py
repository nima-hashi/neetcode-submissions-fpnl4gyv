class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        self.copy = [[0] * (len(matrix[0]) + 1) for i in range(len(matrix) + 1)]
     


        for i in range(1, len(self.copy)):
            for j in range(1, len(self.copy[0])):
                
                self.copy[i][j] = self.copy[i-1][j] + self.copy[i][j-1] + self.matrix[i-1][j-1] - self.copy[i-1][j-1]   
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        leftSide = self.copy[row2+1][col1]
        top = self.copy[row1][col2+1]
        overlap = self.copy[row1][col1]   
        bottomRight = self.copy[row2+1][col2+1]   

        return bottomRight - leftSide - top + overlap

            
       

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)