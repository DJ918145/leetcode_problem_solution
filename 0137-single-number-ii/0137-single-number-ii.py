class Solution(object):
    def singleNumber(self, arr):
        i = 0
        arr.sort()
        while i < len(arr) - 1:
            if arr[i] == arr[i + 1] == arr[i+2]:
                del arr[i]
                del arr[i]
                del arr[i]
            else:
                i += 1

        return arr[0]
        