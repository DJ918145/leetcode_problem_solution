class Solution:
    def generate(self, num):
        if num == 0: #if inserted number is 0
            return []
        if num == 1: #if inserted number is 1
            return [[1]]
        
        prev = self.generate(num - 1) #recursion in this row
        newRow = [1] * num #insert 1 in new row
        
        for i in range(1, num - 1):
            newRow[i] = prev[-1][i - 1] + prev[-1][i] #adding elements in row
        
        prev.append(newRow)
        return prev