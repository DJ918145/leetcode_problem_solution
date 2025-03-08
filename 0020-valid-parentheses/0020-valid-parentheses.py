class Solution(object):
    def isValid(self, s):
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:  # Closing bracket
                if stack and stack[-1] == bracket_map[char]:
                    stack.pop()  # Match found, pop the opening bracket
                else:
                    return False  # No match or stack empty
            else:
                stack.append(char)  # Opening bracket, push to stack
        
        return not stack