class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        maximum_depth = 0
        current_depth = 0
        for char in s:
            if char == '(':
                current_depth+=1
            elif char == ')':
                maximum_depth = max(current_depth, maximum_depth)
                current_depth -= 1
        print(maximum_depth)
        return maximum_depth
        