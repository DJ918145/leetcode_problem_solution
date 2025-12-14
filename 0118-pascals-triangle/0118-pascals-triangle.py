class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: # if the value of numRows is 0 then return []
            return []
        elif numRows == 1: #if the value of numRows is 1 then return [[1]]
            return [[1]]
        else:
            prevRows = self.generate(numRows - 1) # call the recursion process for generating the previous row in the triangle.
            newRow = [1] * numRows #generate the current row of pascal triangle and initialize with 1.
            for i in range(1, numRows - 1):
                newRow[i] = prevRows[-1][i-1] + prevRows[-1][i] #assigning  the value to the row.
            prevRows.append(newRow) # appending the current row in the previous Rows List.
            return prevRows #Returning the previous row
        