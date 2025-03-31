class Solution(object):
    def plusOne(self, arr):
        size = len(arr)
        for i in range(size):
            if(arr[size-1-i]==9):
                arr[size-1-i] = 0
                if i == size-1:
                    arr.insert(0,1)
                    return arr
                else:
                    pass
            else:
                arr[size-1-i] = arr[size-1-i] + 1
                print(arr)
                return arr