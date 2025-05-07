class Solution:
    def setZeroes(self, matrix):
        rowZero = []
        colZero = []

        rows = len(matrix)
        cols = len(matrix[0])

        # Step 1: Save all rows and columns that should be 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowZero.append(i)
                    colZero.append(j)

        # Step 2: Set rows and columns to 0
        for i in range(rows):
            for j in range(cols):
                if i in rowZero or j in colZero:
                    matrix[i][j] = 0