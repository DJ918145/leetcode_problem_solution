class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        result = []
        increment = 2 * (numRows - 1)

        for r in range(numRows):
            for i in range(r, len(s), increment):
                result.append(s[i])
                # Add the diagonal elements for middle rows
                if r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s):
                    result.append(s[i + increment - 2 * r])

        return ''.join(result)