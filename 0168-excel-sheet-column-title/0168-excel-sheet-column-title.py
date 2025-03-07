class Solution(object):
    def convertToTitle(self, columnNumber):
        ans = ""
        while columnNumber > 0:
            columnNumber = columnNumber - 1
            rem = columnNumber % 26
            ans = chr(rem + ord('A')) + ans
            columnNumber = columnNumber // 26
        return ans
        