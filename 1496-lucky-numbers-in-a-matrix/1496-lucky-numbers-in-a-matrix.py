class Solution(object):
    def luckyNumbers (self, matrix):
        lucky_numbers = []
        for i in range(len(matrix)):
            # Find the minimum element in the current row
            min_val = min(matrix[i])
            min_index = matrix[i].index(min_val)
            
            # Check if this minimum element is the maximum in its column
            is_lucky = True
            for j in range(len(matrix)):
                if matrix[j][min_index] > min_val:
                    is_lucky = False
                    break
            
            if is_lucky:
                lucky_numbers.append(min_val)
        
        return lucky_numbers