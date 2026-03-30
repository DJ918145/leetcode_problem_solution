class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morseCar = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        def morse(car):
            return morseCar[ord(car) - 97]
        def convertToMorse(s):
            ans = ""
            for car in s:
                ans+= morse(car)
            return ans
        if len(words)<=1:
            return len(words)
        else:
            for i in range(len(words)):
                words[i] = convertToMorse(words[i])
            return len(set(words))