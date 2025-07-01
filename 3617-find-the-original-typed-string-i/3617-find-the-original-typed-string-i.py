class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        p = 1
        for i in range(len(word)-1):
            if word[i]==word[i+1]:
                p+=1
        return p
        