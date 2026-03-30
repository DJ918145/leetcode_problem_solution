class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morseCar = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        def convertToMorse(s):
            ans = ""
            for car in s:
                ans+= morseCar[ord(car) - 97]
            return ans
        if len(words)<=1:
            return len(words)
        else:
            for i in range(len(words)):
                words[i] = convertToMorse(words[i])
            return len(set(words))