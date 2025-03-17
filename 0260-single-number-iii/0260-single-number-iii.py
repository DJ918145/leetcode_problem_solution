class Solution(object):
    def singleNumber(self, arr):
        arr_size = len(arr)
        arr.sort()
        i = 0
        while 2<=len(arr)-1:
            if arr[i] == arr[i+1]:
                # print(arr)
                del arr[i]
                del arr[i]
                # print(arr)
            else:
                i=i+1
        if len(arr)==2:
            print(arr)
            return arr
        