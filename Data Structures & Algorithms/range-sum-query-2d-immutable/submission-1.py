class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        self.matrix = matrix
        self.allTotals = []
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        total = 0
        m = len(self.matrix)
        n = len(self.matrix[0])

        for x in range(m):
            for y in range(n):
                if (row1 <= x <= row2) and (col1 <= y <= col2):
                    total += self.matrix[x][y]
        #self.allTotals.append(total)
        return total
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)