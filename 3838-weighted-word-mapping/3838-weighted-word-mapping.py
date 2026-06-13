class Solution(object):
    def mapWordWeights(self, words, weights):
        result = []
        
        for word in words:
            total_weight = sum(weights[ord(char) - ord('a')] for char in word)
            mod_weight = total_weight % 26
            mapped_char = chr(ord('z') - mod_weight)
            result.append(mapped_char)
        return "".join(result)
