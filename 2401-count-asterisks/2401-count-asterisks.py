class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        ceck = True
        for i in s:
            if i == '|':
                ceck = not ceck
            if ceck:    
                if i == '*':
                    count+= 1
        return count

        