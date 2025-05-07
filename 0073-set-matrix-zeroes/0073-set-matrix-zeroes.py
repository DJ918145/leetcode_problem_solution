class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        numRows = len(matrix)
        numCols = len(matrix[0])

        cols = set()
        rows = set()

        # if True, set the first col to 0. 
        # We must track this seperately since 0,0 has overloaded meaning otherwise.
        flagForFirstCol = False 

        # propogate zeros to top row and first col for tracking 
        # rows/cols scheduled for deletion
        for row in range(numRows):
            for col in range(numCols):
                if(matrix[row][col] == 0):
                    if(col == 0):
                        flagForFirstCol = True
                    else:
                        matrix[0][col] = 0
                    matrix[row][0] = 0

        # do operations
        for i in range(1,numRows):
            if(matrix[i][0] == 0):
                self.clearRow(matrix, i)
                
        
        for i in range(1,numCols):
            if(matrix[0][i] == 0):
                self.clearCol(matrix, i)

        # special cases
        if(matrix[0][0] == 0):
            self.clearRow(matrix, 0)
        if(flagForFirstCol):
            self.clearCol(matrix, 0)

    def clearRow(self, matrix, row):
        matrix[row] = [0] * len(matrix[0])
    
    def clearCol(self, matrix, col):
        for row in range(len(matrix)):
            matrix[row][col] = 0