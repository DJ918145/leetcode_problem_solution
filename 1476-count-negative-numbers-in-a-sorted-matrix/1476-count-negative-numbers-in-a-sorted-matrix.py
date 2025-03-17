class Solution(object):
    def countNegatives(self, grid):
        negative_count = 0
        for arr in grid:
            for num in arr:
                if num<0:
                    negative_count += 1
        return negative_count
        
        