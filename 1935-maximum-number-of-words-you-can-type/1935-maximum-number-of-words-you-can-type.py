class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        brokenLetters = set(brokenLetters)
        count = 0
        for word in text.split():
            if not any(letter in brokenLetters for letter in word):
                count += 1 
        return count
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        