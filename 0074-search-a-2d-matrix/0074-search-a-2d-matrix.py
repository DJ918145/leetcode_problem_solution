class Solution(object):
    def searchMatrix(self, arr, tar):
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if arr[i][j] == tar:
                    return True
        return False
        